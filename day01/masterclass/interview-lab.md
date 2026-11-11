# Day 01 — Interview and tricky-question lab (answers explained)

Use a 5-second prediction pause before reveal. Labels: B=beginner, I=intermediate, S=senior / production.

1. **[B] What does Spring Boot actually add?** Starters, conditional auto-configuration, opinionated defaults and operational conveniences atop Spring. It does not replace Spring or write the application's business logic.
2. **[B] Spring Framework vs Spring Boot?** Framework supplies programming model/container/MVC; Boot integrates/conventionally configures on top. An app using Boot is still using Spring Framework.
3. **[I] Is IoC the same as DI?** No. IoC is the broader inversion of responsibility; constructor DI is one mechanism for supplying dependencies under that model.
4. **[I] What is the difference between a servlet container and DispatcherServlet?** Tomcat/other container handles servlet hosting and network integration; DispatcherServlet is Spring MVC's front controller handling mapping and dispatch.
5. **[I] Does adding a starter guarantee a given bean?** No. Conditions depend on classpath, application type, properties, existing beans and version-specific behavior.
6. **[S] A service has a controller annotation but isn't mapped. Why?** Check whether it's scanned, application context starts, handler mapping/method/path matches, dependency packaging, profiles and any conditional configuration. Do not assume annotation text alone registers it.
7. **[I] Does @SpringBootApplication equal @RestController?** No. The composed boot annotation covers configuration, component scanning and auto-configuration; controller mapping requires a handler bean and mapping annotations.
8. **[S] What does SpringApplication.run return?** A ConfigurableApplicationContext; from it you can inspect registered beans, but don't casually manipulate the container in business code.
9. **[I] Is every @RestController response JSON?** No. Converter selection, return type and content negotiation decide. Strings are often plain text.
10. **[B] Why a 404 when the app is green?** Process health does not mean your path is mapped. Check HTTP method, path, context path, component scan and handler mappings.
11. **[I] Why not put all Java classes in random packages?** Default scanning generally starts at the boot application's package. Structure is a runtime wiring concern, not merely aesthetic.
12. **[S] How do you investigate a missing auto-configured bean?** Check dependency graph, related conditions/properties, competing bean definitions, active profiles and auto-config diagnostics; do not guess and add arbitrary annotations.
13. **[B] What is the purpose of Maven?** Dependency resolution, repeatable build lifecycle and plugin execution. `mvn test` runs a lifecycle phase; `spring-boot:run` calls a plugin goal.
14. **[I] Why did `mvn test run` fail?** `run` alone is not a known Maven lifecycle phase. Use `mvn test` and separately `mvn spring-boot:run`.
15. **[I] Does @WebMvcTest prove your server listens on localhost:8080?** No. It exercises an MVC slice in a mock servlet environment. Also run a live HTTP smoke test or full integration test when needed.
16. **[S] Why are constructor dependencies easier to test?** Dependencies are explicit; objects can be instantiated with test doubles; no reflective injection needed for straightforward unit tests.
17. **[I] What makes the Greeting record JSON?** Jackson or another installed/configured converter can serialize the record. The record itself isn't intrinsically JSON.
18. **[S] How would you evolve this endpoint safely?** Define response contract, input constraints, negative tests, proper error representations, API compatibility, logs/metrics and deployment checks.
19. **[S] Why is a healthy process not enough for a reliable API?** Readiness, routing, downstream connectivity and business outcomes must all be tested/observed independently.
20. **[S] Does the auto-configured servlet web stack imply WebFlux?** No. Servlet MVC and reactive WebFlux are distinct stacks. Choose intentionally based on dependencies and requirements.

## Scenario 1 — 404 only after refactoring packages
Symptoms: `mvn test` passed previously; endpoint 404 after moving controller.

Investigate: package ancestry, test classpaths, registered handler mappings, effective application configuration. Fix: keep application class in stable root package or use explicit well-scoped configuration. Regression: MVC mapping test + smoke test.

## Scenario 2 — Port 8080 already taken
Symptoms: bind/startup failure, not a 404 from the expected app.

Investigate: identify owning process, verify requested server.port and active profiles. Fix: stop conflicting process or choose another port. Counterexample: changing @GetMapping will not resolve port binding.

## Scenario 3 — Developer expects JSON but gets plain text
Symptoms: `String` returned from @RestController, `Content-Type` is text.

Investigate: return type and converters, Accept/media type. Fix: return a DTO/record for structured JSON and test Content-Type; don't force stringified JSON into an arbitrary String return.

## Interview answer pattern
**Claim → mechanism → minimal example → counterexample → production implication**. Avoid one-line memorized definitions.
