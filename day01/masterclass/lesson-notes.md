# Day 01 — Instructor's detailed explanation notes

Use these notes to construct a narrated *lesson*, not a fast-slide presentation. Every bold concept should be explained with an example, not read as bullets.

## 1. Why Spring Boot? (0–3 min)

**Opening scenario.** You have joined a team building a food-ordering service. A customer requests a restaurant menu and places an order. What is the backend responsible for? It receives requests, validates information, executes business logic, calls persistence/services, and sends a response. Not all these responsibilities belong to the web framework; Spring helps compose application components, while Boot reduces repetitive setup.

**Analogy.** Spring Framework is a set of engineered building blocks; Spring Boot adds a reasonable starting configuration. Don't claim Boot builds a complete production-ready application for free.

**Question to pause on:** If we can write Java classes ourselves, why do we need a framework? *Answer:* consistency, dependency management, testability, shared infrastructure, and reduced manual assembly. Frameworks also impose trade-offs: abstraction, configuration complexity and version constraints.

## 2. Foundations for total beginners (3–8 min)

Explain each word separately:
- **Client:** software that sends a request (browser, mobile app, another service).
- **Server:** receives and processes requests; network listener isn't the same as controller.
- **HTTP:** request/response protocol. A request includes method, path, headers and possibly a body. A response includes status, headers and body.
- **GET:** conventionally retrieve data; avoid side-effectful business mutations on GET.
- **URL path:** `/api/greetings`; **query parameter:** `name=Alex`.
- **JSON:** data format (objects, properties, strings); not the same thing as Java.
- **JAR:** packaged Java application. **JDK** compiles and runs Java; **Maven** resolves dependencies, executes build lifecycle goals/plugins.

Use a request card:

```http
GET /api/greetings?name=Alex HTTP/1.1
Host: localhost:8080
Accept: application/json
```

Discuss *what* each part means; do not teach HTTP headers as memorization.

## 3. Spring Framework vs Spring Boot (8–14 min)

**Spring Framework** provides an IoC container, DI, AOP infrastructure, Spring MVC, transaction abstractions and integration components. **Spring Boot** uses Spring Framework and convention-based/conditional auto-configuration, starters and application runtime conveniences.

**IoC:** object creation/wiring responsibility can move from application code to a container. **DI:** required objects are supplied rather than each class constructing everything itself. They are closely related, but not synonyms.

Example:

```java
class OrderService {
    private final PaymentGateway gateway;
    OrderService(PaymentGateway gateway) { this.gateway = gateway; }
}
```

Discuss constructor injection: explicit dependencies, easier unit tests, consistent initialization. Distinguish plain Java constructor injection from Spring-managed bean wiring.

**Misconception:** Boot is not "Spring without XML"; Spring Framework already supports Java configuration.

**Check:** Could you create an HTTP app in Spring Framework without Boot? Yes, but more manual configuration and dependency setup may be required.

## 4. Maven project anatomy (14–20 min)

Walk `pom.xml` line-by-line:
- `parent` provides managed dependency/plugin versions and defaults; pin the exact version for reproducibility.
- `spring-boot-starter-webmvc` adds the servlet MVC web stack; starter is a dependency aggregator, not a separate framework.
- `spring-boot-starter-webmvc-test` supplies compatible test support for this lesson.
- `spring-boot-maven-plugin` handles application packaging/running goals.
- `java.version` chooses project Java baseline; verify actual JDK locally.

`src/main/java` production, `src/test/java` tests; `target/` generated output and not tracked in Git.

Compare `mvn clean test` (compile + test), `mvn package` (package), `mvn spring-boot:run` (plugin goal). Demonstrate why `mvn test run` is wrong: `run` isn't an unqualified Maven lifecycle phase.

## 5. Boot startup X-Ray (20–28 min)

Walk sequentially:
1. JVM calls `main` and `SpringApplication.run(...)`.
2. Spring creates/prepares appropriate `ApplicationContext` for application type and processes environment/properties.
3. Configuration and bean definitions are registered; component scanning begins from the main application's package by default.
4. Conditional auto-configurations react to dependencies, properties, missing/present beans and application type.
5. Beans are instantiated/initialized subject to lifecycle/eager vs lazy behavior, with post-processors and proxy behavior where relevant.
6. A servlet web application sets up/starts its embedded web server during context initialization; handlers are registered.
7. On successful startup, the app serves HTTP requests.

**Precision:** This is a teaching simplification, not an exact universal ordering of every Spring callback. Some configuration parsing, context refresh, post-processors, events and lifecycle callbacks occur at different points. Do not imply every bean is eagerly constructed.

**Architecture diagram:** Client → web server → filter chain → DispatcherServlet → HandlerMapping → HandlerAdapter → controller → return-value handling / HttpMessageConverter → response.

**Trick:** `@SpringBootApplication` is a composed annotation. It doesn't itself make a controller. The web starter supplies MVC infrastructure through dependencies and configuration.

**Production tip:** inspect auto-configuration conditions and startup logs/Actuator rather than guessing which bean was created.

## 6. API walkthrough (28–37 min)

Read the actual `GreetingController` file:
- `@RestController`: controller + response body semantics.
- `@GetMapping("/api/greetings")`: maps HTTP GET to this handler.
- `@RequestParam(defaultValue="Developer")`: query param binding with default when not supplied (and generally when empty with a default).
- `record Greeting(String message, String course)`: immutable data carrier by design; Jackson can serialize its components when configured.
- String concatenation only for the demo, not a full input-validation strategy.

Use executed browser response:

```json
{"message":"Hello, Alex!","course":"Spring Boot Simplified"}
```

Explain 200 vs 404; what 404 says and *doesn't* say. Talk through controller return → MVC return-value handling → configured converter → JSON, not "Tomcat converts Java to JSON".

**Hands-on pause:** change `name` to the viewer's first name. Then remove the query parameter and predict the outcome before showing default greeting.

## 7. Automated tests (within 28–37 min)

Explain difference between *running code manually* and *automatically asserting behavior*. In `@WebMvcTest(GreetingController.class)`, a web MVC slice is loaded, not necessarily the full application graph. `MockMvc` performs mock servlet requests in a Spring MVC test context; it does not prove an externally bound network port works.

Explain each assertion: `status().isOk()`, JSON property equality. Mention tests are designed to catch regression if mapping/default/message changes.

Learner's reported result: 2 tests, 0 failures, 0 errors. For the video, capture fresh output after `mvn clean test`.

## 8. Break / debug / fix lab (37–43 min)

**Experiment A — Wrong URL:** `/api/greeting` → 404. Check mapping and method, not random JVM flags.

**Experiment B — Port in use:** start a second instance on port 8080. Server may fail to bind. Resolution: stop competing process or configure different `server.port`. Make clear this is not the same failure as a controller 404.

**Experiment C — Component scan:** move controller to an unrelated package without intentionally adding scan configuration; a missing endpoint can result. Correct package structure or explicit import/scanning with well-understood boundaries.

**Debug method:** observe error → isolate layer → form hypothesis → check logs/mappings → change one variable → rerun test.

## 9. Senior/architect nuance (43–49 min)

**Auto-configuration:** conditions may cause configuration to back off if user beans exist. Not a guarantee that every bean always "magically" appears.

**Embedded server vs Spring MVC:** embedded Tomcat is a servlet container; `DispatcherServlet` is Spring MVC's front controller. Avoid calling Tomcat "the controller".

**Not everything is JSON:** `String` responses frequently use StringHttpMessageConverter and plain text. Media types/content negotiation matter.

**Package design:** keep boot application class in a sensible parent package so scanning is clear. Don't use wildcard scan of unrelated packages as a default fix.

**HTTP correctness:** GET should be safe; avoid using it for money transfers or state-changing tasks.

**Observability:** distinguish readiness/health of process from existence of every route. An app can start successfully but have an incorrect mapping.

## 10. Interview lab and revision (49–60 min)

Run [interview-lab.md](interview-lab.md) as question → 5–10 second thinking pause → explain → counterexample. Distinguish which questions are basics, traps, or production scenarios.

**Final challenge:** Explain how GET `/api/greetings?name=Alex` becomes JSON in 60 seconds without notes. Then add another endpoint with a test. Use [revision-sheet.md](revision-sheet.md) and [practical-labs.md](practical-labs.md).

## Suggested visual style

Dark navy, accessible high-contrast typography, consistent green for successful flow, amber for decisions, red only for errors. Replace generic decorative animations with precise state changes. Each arrow must correspond to a meaningful call or data movement. Use lower-thirds for terms, large code font, and no unreadable terminal walls.

## Source of truth

https://docs.spring.io/spring-boot/reference/
https://docs.spring.io/spring-framework/reference/web/webmvc.html
https://docs.spring.io/spring-framework/reference/core/beans.html
