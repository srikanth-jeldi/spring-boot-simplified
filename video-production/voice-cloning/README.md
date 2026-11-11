# OpenVoice V2 private voice-cloning pilot

**Status:** Generator and setup instructions added. Not yet executed on the user's Windows laptop; no cloned audio generated or quality-verified.

**Privacy:** Keep your personal WAV and extracted speaker embeddings on your own computer, NEVER in this public GitHub repository. The repository only stores source code.

## Recommended: isolated WSL2 Linux environment

Official OpenVoice installation targets Linux and Python 3.9. Windows support is community-maintained. Avoid breaking your existing working Python 3.12 Kokoro environment. Python 3.9 is end-of-support, so isolate this experiment; do not run a public service with it.

Windows PowerShell, admin for first install:

    wsl --install -d Ubuntu

After restart if requested, launch Ubuntu. Install Miniconda plus git and required system libraries if missing. Follow official instructions: https://github.com/myshell-ai/OpenVoice/blob/main/docs/USAGE.md

In Ubuntu:

    conda create -n openvoice python=3.9
    conda activate openvoice
    git clone https://github.com/myshell-ai/OpenVoice.git
    cd OpenVoice
    pip install -e .
    pip install git+https://github.com/myshell-ai/MeloTTS.git
    python -m unidic download

Download V2 checkpoints from https://myshell-public-repo-host.s3.amazonaws.com/openvoice/checkpoints_v2_0417.zip and extract to OpenVoice/checkpoints_v2 following official directions.

Run from the upstream OpenVoice directory. For Windows voice reference E:\SpringBootVoice\my_voice_clean.wav:

    python /mnt/e/SpringBootVoice/spring-boot-simplified/video-production/voice-cloning/clone_voice.py --reference /mnt/e/SpringBootVoice/my_voice_clean.wav --checkpoint-dir checkpoints_v2 --output /mnt/e/SpringBootVoice/my_cloned_voice.wav

WSL maps E: to /mnt/e. If the Melo source speaker key EN-US is absent, the script prints available speakers; choose with --speaker.

## Review gate

Listen to the cloned 45–60 second technical narration before switching from Kokoro Michael. Compare similarity to your voice, English pronunciation, naturalness, distortions, and CPU speed. OpenVoice V2 uses base TTS + tone-color conversion, which does not guarantee identical accent or expressive style. First CPU setup may require dependency troubleshooting.

Sources: https://github.com/myshell-ai/OpenVoice/blob/main/demo_part3.ipynb and https://github.com/myshell-ai/OpenVoice/blob/main/docs/USAGE.md

Only clone voices you have authorization to use. Check licenses of any additional dependencies separately.
