# Day 01 — Hands-on labs with solutions

## Lab A (Beginner): Change the input
**Task:** Run GET `/api/greetings?name=Alex` and without `name`. Predict response before each call.

**Solution:** Alex → `Hello, Alex!`; missing parameter → `Hello, Developer!` because defaultValue is provided.

## Lab B (Beginner): Add an endpoint
**Task:** Add `GET /api/health-message` returning structured JSON with two fields, without changing original contract.

Example solution (add to the existing controller):

```java
@GetMapping("/api/health-message")
public HealthMessage health() {
    return new HealthMessage("UP", "Day 01");
}
public record HealthMessage(String status, String lesson) {}
```

**Acceptance:** `curl.exe -i http://localhost:8080/api/health-message` yields HTTP 200 with status=UP, lesson=Day 01. This is a demonstration endpoint, **not** a real liveness/readiness indicator.

## Lab C (Intermediate): Add an MVC test
Append to `GreetingControllerTest`:

```java
@Test
void healthMessageReturnsJson() throws Exception {
    mvc.perform(get("/api/health-message"))
       .andExpect(status().isOk())
       .andExpect(jsonPath("$.status").value("UP"))
       .andExpect(jsonPath("$.lesson").value("Day 01"));
}
```

**Acceptance:** `mvn clean test` passes 3 tests after you implement both endpoint and test. Do not claim 3 passed until executed.

## Lab D (Intermediate): Trigger and fix 404
**Task:** Call singular path `/api/greeting`. Compare response with plural path. Diagnose before changing code.

**Solution:** The mapping is `/api/greetings`; update request or mapping intentionally. A 404 does not imply the JVM or web server has crashed.

## Lab E (Experienced): Understand scan boundaries
**Task:** Move GreetingController into `com.otherpackage`, leaving boot main class where it is, and observe the registered mappings. Restore afterward.

**Reason:** by default component scanning starts from the boot application class's package and descendants. A controller outside that scope won't normally be discovered.

**Solution options:** keep controller under `com.springbootsimplified.day01`, or explicitly register/import additional configuration. Prefer good package structure over indiscriminate broad scanning.

## Lab F (Experienced): Content negotiation trap
**Task:** Add handler returning a plain String:

```java
@GetMapping("/api/plain")
public String plain() { return "hello"; }
```

Call with `curl.exe -i`; observe content type. Compare with the Greeting record endpoint.

**Expected learning:** return-value type and available message converters affect the response. Never assert all @RestController results become JSON.

## Final mastery check
- Explain all code lines of the original project without reading notes.
- Run every lab on your machine; keep the original two tests green.
- Document one bug, its root cause, the smallest fix, and how to prevent a regression.
- Answer at least 15 of 20 interview questions with reasoning, not one-line recall.
