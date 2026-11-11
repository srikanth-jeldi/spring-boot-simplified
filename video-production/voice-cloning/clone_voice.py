from pathlib import Path
import argparse
import torch
from openvoice import se_extractor
from openvoice.api import ToneColorConverter
from melo.api import TTS

TEXT = (
    "Here is a Spring Boot interview challenge. "
    "A service method calls another method in the same class. "
    "The second method has the transactional annotation. "
    "Will Spring automatically begin a new transaction? "
    "In default proxy based transaction management, not necessarily. "
    "The internal call bypasses the Spring proxy, so that annotation is not intercepted. "
    "An existing transaction can still be active. "
    "Move the transactional method into another Spring managed bean, and invoke it through its proxy. "
    "This is why understanding internals matters."
)

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--reference", required=True)
    p.add_argument("--checkpoint-dir", default="checkpoints_v2")
    p.add_argument("--output", default="outputs_v2/my_cloned_voice.wav")
    p.add_argument("--speaker", default="EN-US")
    args = p.parse_args()
    reference = Path(args.reference).expanduser().resolve()
    ckpt = Path(args.checkpoint_dir).resolve()
    output = Path(args.output).resolve()
    if not reference.is_file():
        raise SystemExit(f"Reference recording not found: {reference}")
    if not (ckpt / "converter" / "checkpoint.pth").is_file():
        raise SystemExit("Missing OpenVoice V2 checkpoints; see README.")
    output.parent.mkdir(parents=True, exist_ok=True)
    device = "cuda:0" if torch.cuda.is_available() else "cpu"
    print("Device:", device)
    converter = ToneColorConverter(str(ckpt / "converter" / "config.json"), device=device)
    converter.load_ckpt(str(ckpt / "converter" / "checkpoint.pth"))
    target_se, _ = se_extractor.get_se(str(reference), converter, vad=True)
    model = TTS(language="EN_NEWEST", device=device)
    speakers = model.hps.data.spk2id
    print("Available source speakers:", list(speakers))
    if args.speaker not in speakers:
        raise SystemExit("Unknown source speaker; choose one from the printed keys.")
    speaker_key = args.speaker.lower().replace("_", "-")
    source_file = ckpt / "base_speakers" / "ses" / (speaker_key + ".pth")
    if not source_file.is_file():
        raise SystemExit(f"Missing source speaker embedding: {source_file}")
    source_se = torch.load(str(source_file), map_location=device, weights_only=False)
    base_file = output.parent / "base_voice.wav"
    model.tts_to_file(TEXT, speakers[args.speaker], str(base_file), speed=1.0)
    converter.convert(audio_src_path=str(base_file), src_se=source_se, tgt_se=target_se, output_path=str(output), message="@SpringBootSimplified")
    print("Cloned voice sample:", output)

if __name__ == "__main__":
    main()
