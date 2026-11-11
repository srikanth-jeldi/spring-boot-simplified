# Spring Boot Simplified — Video Production

This folder is the source of truth for video assets and rendering code.

**STATUS / SCOPE:** Existing `build_video.py` produces a short **slide-based review preview**, not the 50–60-minute in-depth Day 01 masterclass. Do not label this output as the final YouTube lesson or pad it with repeated audio. Full masterclass content: [Day 01 masterclass](../day01/masterclass/README.md). Long-form narration, timing, animation and voice QA are still required. **No ChatGPT sandbox downloads needed.** Run everything on your Windows PC.

## Day 01 video

Generates a **narrated, scene-based 1280×720 MP4** with Kokoro `am_michael`, readable code, request X-Ray, break/fix and tricky interview questions. It is a **review cut**, not an automatically quality-approved YouTube master.

### Requirements

- Windows, Python 3.12 with your existing Kokoro virtual environment
- FFmpeg available on PATH (test: `ffmpeg -version`; if missing: `winget install Gyan.FFmpeg`, reopen PowerShell)
- Kokoro already working with `KPipeline`
- Pillow, NumPy, soundfile: `python -m pip install -r video-production/requirements.txt`

### Commands (from E:\SpringBootVoice\spring-boot-simplified)

```powershell
git pull
cd video-production
E:\SpringBootVoice\.venv\Scripts\python.exe -m pip install -r requirements.txt
E:\SpringBootVoice\.venv\Scripts\python.exe build_video.py
```

If your working venv lives instead at `E:\SpringBootVoice\spring-boot-simplified\.venv`, use its Python path instead.

Expected output:

```text
video-production/output/day01_video01_michael.mp4
video-production/output/day01_video01_michael.wav
video-production/output/scene_01.png ... scene_10.png
```

Play it:

```powershell
Start-Process .\output\day01_video01_michael.mp4
```

**Note:** Videos are generated locally and excluded from Git to keep the repository lightweight. You can manually upload approved MP4s to GitHub Releases or YouTube. Source code, narration and scene templates remain version-controlled.

### Quality gates before publication

- Watch entire video for TTS pronunciation and weird pauses.
- Check text fits and remains readable on mobile.
- Check claims against [Spring Boot docs](https://docs.spring.io/spring-boot/reference/).
- Verify the code project with `mvn clean test`.
- Do not replace runtime capture with fictional terminal screenshots.
- No copyrighted music or unrelated visuals.

**Important distinction:** Audio loudness normalization does not convert synthetic speaking style into human emotion. Improve scripts and compare models if Michael remains insufficient.
