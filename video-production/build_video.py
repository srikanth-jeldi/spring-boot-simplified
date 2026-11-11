"""Spring Boot Simplified — Day 01 locally rendered video pilot.
Requires working Kokoro, Pillow, NumPy, soundfile and ffmpeg on PATH.
This is a scene-based preview, not a final motion-graphics master.
"""
from pathlib import Path
import shutil
import subprocess
import textwrap
import numpy as np
import soundfile as sf
from PIL import Image, ImageDraw, ImageFont
from kokoro import KPipeline

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "output"
OUTPUT.mkdir(exist_ok=True)
SAMPLE_RATE = 24000
WIDTH, HEIGHT = 1280, 720
VOICE = "am_michael"
SPEED = 0.96

# Each slide pairs visible teaching content with original narration.
SCENES = [
    {
        "title": "SPRING BOOT — FROM THE INSIDE OUT",
        "tag": "01 / THE PROBLEM",
        "body": [
            "Imagine building a food-ordering backend.",
            "You need HTTP endpoints, a web server,",
            "configuration and business components.",
            "What should you configure by hand?"
        ],
        "narration": "Imagine you're building a food ordering backend. You need HTTP endpoints, a web server, configuration, and business components. What should you configure by hand, and what should the framework prepare for you? That's the problem Spring Boot helps solve."
    },
    {
        "title": "SPRING FRAMEWORK versus SPRING BOOT",
        "tag": "02 / THE DIFFERENCE",
        "body": [
            "Spring Framework: IoC, dependency injection, MVC",
            "Spring Boot: starters + conditional auto-configuration",
            "Boot is built ON Spring. It does not replace Spring."
        ],
        "narration": "Spring Framework gives us the underlying programming model: dependency injection, managed beans, web MVC, and much more. Spring Boot is built on Spring. It adds dependency starters, auto configuration, and sensible defaults. Boot is not a separate replacement for the Spring Framework."
    },
    {
        "title": "WHAT DOES THE ANNOTATION ENABLE?",
        "tag": "03 / STARTUP",
        "code": [
            "@SpringBootApplication",
            "public class Day01Application {",
            "    public static void main(String[] args) {",
            "        SpringApplication.run(Day01Application.class, args);",
            "    }",
            "}"
        ],
        "body": ["Configuration • Component scanning • Auto-configuration"],
        "narration": "The Spring Boot application annotation combines three key ideas: configuration, component scanning, and enabling auto configuration. The main method then calls Spring Application dot run, which bootstraps the application context. This annotation does not directly handle HTTP requests."
    },
    {
        "title": "AUTO-CONFIGURATION IS CONDITIONAL",
        "tag": "04 / BEHIND THE SCENES",
        "body": [
            "Dependencies on classpath + application properties",
            "                  ↓",
            "             Conditions",
            "                  ↓",
            "          Bean configuration",
            "Not every classpath entry creates a bean."
        ],
        "narration": "Auto configuration is not unexplained magic. Spring Boot checks classpath contents, configuration properties, and existing beans. Conditional configuration can then register useful infrastructure. This also means that including a starter does not guarantee every imaginable bean will be created."
    },
    {
        "title": "HTTP REQUEST X-RAY",
        "tag": "05 / INTERNAL EXECUTION",
        "body": [
            "Browser  →  Tomcat  →  DispatcherServlet",
            "                             ↓",
            "                    Handler mapping",
            "                             ↓",
            "                     REST Controller",
            "                             ↓",
            "                  JSON HTTP response"
        ],
        "narration": "Let's trace one request. Your browser sends an H T T P request. The embedded servlet server, typically Tomcat in this setup, accepts it. Spring M V C's Dispatcher Servlet uses handler mappings to find a controller. The controller returns a value, and a configured message converter can serialize that value into the response. Security filters and interceptors may add further steps in a real application."
    },
    {
        "title": "YOUR FIRST WORKING API",
        "tag": "06 / REAL JAVA CODE",
        "code": [
            "@RestController",
            "class GreetingController {",
            "  @GetMapping(\"/api/greetings\")",
            "  Greeting hello(@RequestParam(defaultValue=\"Developer\")",
            "                 String name) {",
            "    return new Greeting(\"Hello, \" + name + \"!\",",
            "                        \"Spring Boot Simplified\");",
            "  }",
            "  record Greeting(String message, String course) {}",
            "}"
        ],
        "narration": "Here is our real controller. Rest Controller marks it as a web controller whose return values form response bodies. Get Mapping connects this method to slash API slash greetings. Request Param reads a name from the query string, with Developer as the default. Returning a Java record allows a configured JSON converter to serialize its fields."
    },
    {
        "title": "INPUT → OUTPUT (VERIFIED LOCALLY)",
        "tag": "07 / RUN IT",
        "code": [
            "GET /api/greetings?name=Alex",
            "",
            '{',
            '  "message": "Hello, Alex!",',
            '  "course": "Spring Boot Simplified"',
            '}'
        ],
        "body": ["User confirmed browser response and 2 passing tests."],
        "narration": "We ran this endpoint on the local machine. When name equals Alex, the response message becomes Hello, Alex. The viewer also verified two automated tests passed with zero failures. Notice that this is a simple read-only API, not yet a database or production deployment."
    },
    {
        "title": "BREAK IT — LEARN THE FAILURE",
        "tag": "08 / DEBUGGING",
        "code": [
            "Works:  GET /api/greetings",
            "Fails:  GET /api/greeting",
            "",
            "Result: HTTP 404 — route not found"
        ],
        "body": [
            "Correct the requested URL or change the mapping.",
            "Do not change random server settings."
        ],
        "narration": "Now let's break it deliberately. Call slash API slash greeting, singular, instead of greetings, plural. The application can be running perfectly, yet Spring returns a four oh four because that route is not mapped. The fix is to correct the requested path, or intentionally update the mapping and its tests."
    },
    {
        "title": "THE EXPERIENCED-DEVELOPER TRAP",
        "tag": "09 / INTERVIEW CHALLENGE",
        "body": [
            "Does @RestController guarantee JSON?",
            "No. Return type, available message converters",
            "and content negotiation affect the response.",
            "A String return value may be plain text."
        ],
        "narration": "Here's a tricky interview question. Does Rest Controller guarantee that every return value will be JSON? No. Spring chooses how to write the response using the return type, configured message converters, and content negotiation. For example, a String return value often becomes plain text. Knowing the mechanism is more useful than memorizing the annotation."
    },
    {
        "title": "RECAP — UNDERSTAND, BUILD, BREAK",
        "tag": "10 / YOUR CHALLENGE",
        "body": [
            "Spring = framework and container",
            "Boot = startup conventions and auto-configuration",
            "Tomcat = servlet web server",
            "DispatcherServlet = Spring MVC front controller",
            "Challenge: add /api/health-message + one test",
            "GitHub: srikanth-jeldi/spring-boot-simplified"
        ],
        "narration": "Let's recap. Spring provides the framework and managed components. Boot simplifies configuration and application startup. Tomcat serves servlet H T T P traffic, and the Dispatcher Servlet routes requests through Spring M V C. Your challenge is to add a second endpoint and write a test. Follow the complete working lesson on our GitHub repository."
    }
]

def font(size=36, bold=False, mono=False):
    fonts = Path("C:/Windows/Fonts")
    candidates = (
        ["consolab.ttf", "lucon.ttf"] if mono else
        (["segoeuib.ttf", "arialbd.ttf"] if bold else ["segoeui.ttf", "arial.ttf"])
    )
    for filename in candidates:
        p = fonts / filename
        if p.exists():
            return ImageFont.truetype(str(p), size)
    return ImageFont.load_default()

def render_slide(scene, i):
    im = Image.new("RGB", (WIDTH, HEIGHT), (8, 23, 39))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((46, 38, 1234, 680), 22, fill=(13, 39, 58), outline=(40, 100, 113), width=2)
    d.rounded_rectangle((70, 65, 360, 106), 11, fill=(28, 87, 77))
    d.text((88, 72), scene["tag"], font=font(19, bold=True), fill=(189, 244, 210))
    title = scene["title"]
    for j, line in enumerate(textwrap.wrap(title, 36)):
        d.text((78, 135 + j * 56), line, font=font(40, bold=True), fill=(244, 249, 255))
    y = 245
    if scene.get("code"):
        lines = scene["code"]
        h = min(345, 35 + 34 * len(lines))
        d.rounded_rectangle((80, y, 1198, y + h), radius=16, fill=(7, 19, 29), outline=(45, 122, 135), width=2)
        for k, line in enumerate(lines):
            d.text((100, y + 18 + 34 * k), line, font=font(22, mono=True), fill=(157, 237, 193) if line.strip().startswith("@") else (226, 239, 249))
        y += h + 24
    if scene.get("body"):
        for line in scene["body"]:
            if y > 623: break
            d.text((94, y), line, font=font(25, bold=False), fill=(203, 226, 236))
            y += 39
    d.line((80, 643, 1200, 643), fill=(46, 83, 97), width=2)
    d.text((84, 652), "SPRING BOOT SIMPLIFIED  •  DAY 01", font=font(16, bold=True), fill=(118, 191, 174))
    d.text((1088, 652), f"{i:02d} / {len(SCENES):02d}", font=font(16), fill=(194, 215, 227))
    path = OUTPUT / f"scene_{i:02d}.png"
    im.save(path)
    return path

def create_audio(pipeline, scene, i):
    chunks = []
    for _, _, audio in pipeline(scene["narration"], voice=VOICE, speed=SPEED):
        chunks.append(np.asarray(audio, dtype=np.float32))
    if not chunks:
        raise RuntimeError(f"No TTS audio in scene {i}")
    return np.concatenate(chunks)

def main():
    if not shutil.which("ffmpeg"):
        raise SystemExit("FFmpeg not found. Install with: winget install Gyan.FFmpeg ; reopen PowerShell.")
    print("Loading Kokoro Michael…")
    pipeline = KPipeline(lang_code="a", repo_id="hexgrad/Kokoro-82M")
    slides, audios, durations = [], [], []
    for i, scene in enumerate(SCENES, 1):
        print(f"Scene {i}/{len(SCENES)}: {scene['title']}")
        slides.append(render_slide(scene, i))
        wav = create_audio(pipeline, scene, i)
        pause = 0.8 if i == len(SCENES) else 0.48
        wav = np.concatenate([wav, np.zeros(int(SAMPLE_RATE * pause), dtype=np.float32)])
        audios.append(wav)
        durations.append(len(wav) / SAMPLE_RATE)
    audio = np.concatenate(audios)
    peak = float(np.max(np.abs(audio)))
    if peak > 0: audio *= min(1.2, 0.92 / peak)
    wav_path = OUTPUT / "day01_video01_michael.wav"
    sf.write(wav_path, audio, SAMPLE_RATE, subtype="PCM_16")
    concat_file = OUTPUT / "scenes.txt"
    with concat_file.open("w", encoding="utf-8") as f:
        for path, duration in zip(slides, durations):
            # Forward-slash absolute Windows paths are understood by ffmpeg.
            f.write(f"file '{path.as_posix()}'\n")
            f.write(f"duration {duration:.4f}\n")
        f.write(f"file '{slides[-1].as_posix()}'\n")
    output_path = OUTPUT / "day01_video01_michael.mp4"
    cmd = [
        "ffmpeg", "-hide_banner", "-y", "-loglevel", "error",
        "-safe", "0", "-f", "concat", "-i", str(concat_file),
        "-i", str(wav_path), "-r", "24",
        "-c:v", "libx264", "-pix_fmt", "yuv420p",
        "-c:a", "aac", "-b:a", "160k",
        "-shortest", "-movflags", "+faststart",
        str(output_path)
    ]
    print("Rendering MP4 with FFmpeg…")
    subprocess.run(cmd, check=True)
    print(f"SUCCESS: {output_path}")
    print(f"Audio duration: {len(audio) / SAMPLE_RATE:.1f} sec")
    print("This is a narrated slides review cut, not a full animation master.")

if __name__ == "__main__":
    main()
