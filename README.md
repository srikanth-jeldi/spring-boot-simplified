# Spring Boot Simplified

**Understand it. Visualize it. Build it. Break it. Master it.**

An English-first Spring Boot learning series for beginners **and** experienced Java engineers. Every lesson includes: **What → Why → How → Internals → Runnable Code → Break/Fix → Production → Interview**.

## Day 01 — What is Spring Boot?

**New full-course standard:** 50–60-minute concept-to-internals masterclass, followed by hands-on practice and an expert interview lab. The old 4-minute narrated preview is *not* an adequate full lesson. See [Day 01 masterclass materials](day01/masterclass/README.md).

- [Lesson guide](day01/README.md)
- [Working REST API project](day01/lesson01/)
- [Interview & tricky questions](day01/interview-questions.md)
- [Video narration & storyboard](day01/video01-narration.md)

## Run the first example

Prerequisites: **JDK 17+** and **Maven 3.9+**.

```bash
cd day01/lesson01
mvn test
mvn spring-boot:run
```

Test: `http://localhost:8080/api/greetings?name=Alex`

Expected: `{"message":"Hello, Alex!","course":"Spring Boot Simplified"}`

**Status:** GitHub source published; Maven build/tests have **not yet been executed** in the authoring environment. Do not claim this lesson has passed CI until `mvn test` passes.

## Teaching rules

1. Explain the problem before the annotation.
2. Show precise request/bean lifecycle diagrams; don't invent internals.
3. Pair each concept with a working example, intentional failure and fix.
4. Distinguish defaults from guaranteed behavior and version-dependent details.
5. Include senior/architect-level traps without overwhelming beginners.
6. Use human-reviewed narration, not unapproved robotic audio.

Official docs: https://docs.spring.io/spring-boot/reference/
