# DAY 01 MASTERCLASS — Spring Boot From Zero to Internal Architecture

**Status:** Revised curriculum and teaching material. The earlier ~4-minute preview is **not** the finished lesson. The complete 50–60-minute narrated MP4 remains **not produced**.

**Learning outcome:** A newcomer can run/explain the first API, and an experienced developer can describe startup, auto-configuration conditions, request dispatch, scope boundaries, diagnostics and trade-offs accurately.

## The 55–60-minute production plan

| Time | Segment | Beginner goal | Experienced / interview depth |
|---|---|---|---|
| 00:00–03:00 | Hook: build an ordering backend | Understand what a backend does | Identify infrastructure vs business logic |
| 03:00–08:00 | Prerequisites: Java, HTTP, server | URL, request/response, JSON | HTTP method semantics, serialization |
| 08:00–14:00 | Framework vs Spring vs Spring Boot | What each means | IoC vs DI, Boot on top of Spring |
| 14:00–20:00 | Project structure and Maven | pom.xml, dependencies, main class | dependency starters vs BOM, transitive classpath |
| 20:00–28:00 | Startup X-Ray | How application starts | ApplicationContext, scanning, conditional auto-config, server start |
| 28:00–37:00 | Working API and test | Create GET endpoint | MVC dispatch, handler mapping, return converters |
| 37:00–43:00 | Break → Debug → Fix lab | Diagnose 404 and port errors | Scope and configuration diagnostics |
| 43:00–49:00 | Behind-the-scenes traps | Defaults vs guarantees | Bean registration, text vs JSON, condition back-off |
| 49:00–56:00 | 15 interview questions, pause/reveal | Recall fundamentals | Scenario questions and root-cause explanations |
| 56:00–60:00 | Revision challenge and recap | Explain without notes | Trade-offs, edge cases, follow-up homework |

This is a *planned runtime*, not an assertion that an MP4 exists or that the current narration reaches it. Audio duration must be measured after synthesis.

## Teaching rules (mandatory)

1. Explain every new term before using it. Show its purpose, not just its definition.
2. Each major concept: analogy → precise model → animated execution → code → input/output → what-if failure → interviewer asks why.
3. Show **real executed commands** and reproducible responses, or label a diagram as illustrative.
4. Every code block has accompanying explanation of why it exists and what fails when removed.
5. Every tricky question has a reasoned answer, exception/qualification and a related production symptom.
6. Narration should be understandable when heard without looking at the slide; slides must remain readable on a phone.
7. No artificial filler to reach 60 minutes. Add worthwhile examples, guided exercises and Q&A.
8. Human review of Kokoro Michael pronunciation required before the release.

## Run existing verified example

```powershell
cd day01/lesson01
mvn clean test
mvn spring-boot:run
```

The user ran the two tests successfully on Windows (2 run, 0 failure, 0 error). In a second terminal:

```powershell
curl.exe -i "http://localhost:8080/api/greetings?name=Alex"
curl.exe -i "http://localhost:8080/api/greetings"
curl.exe -i "http://localhost:8080/api/greeting"
```

Expected results: first request is 200 with Alex; second is 200 with Developer; third is normally a 404 unless mapping changes. The video must record a fresh run rather than fabricate console footage.

## Viewing levels

- **Beginner track:** 00:00–43:00, plus recap.
- **Experienced track:** 20:00–60:00, focus on internals, pitfalls, and interview drills.
- **Revision track:** [revision-sheet.md](revision-sheet.md) + 15-question timed quiz.

## Files in this masterclass

- [Detailed scene-by-scene teaching notes](lesson-notes.md)
- [Interview and tricky questions with solutions](interview-lab.md)
- [Fast revision sheet](revision-sheet.md)
- [Hands-on labs and acceptance checks](practical-labs.md)

## Production status / release gates

- [x] Spring Boot example and automated tests run successfully by learner
- [x] 60-minute lesson plan + supporting materials written
- [ ] Full 6,000–8,000-word natural English narration written and timing verified
- [ ] 50–60-minute audio synthesized using approved Michael voice
- [ ] Code-capture segments, animated diagrams, timed subtitles
- [ ] Published review MP4 with audio sync, technical QA, readability checks

**Important:** A 4-minute slideshow should never be described as this masterclass. Do not extend narration by looping or slowing audio.
