# Day 01 — 10-minute revision sheet

## Say these definitions aloud
- **Spring Framework:** application framework with IoC container, DI, MVC and more.
- **Spring Boot:** convention-driven tooling, starters and conditional auto-configuration built on Spring.
- **ApplicationContext:** Spring's container for configuration and managed components.
- **Bean:** object registered/managed by Spring, subject to applicable lifecycle and scopes.
- **Auto-configuration:** conditionally contributes configuration based on app context and dependencies.
- **DispatcherServlet:** Spring MVC front controller, separate from embedded Tomcat.
- **Controller mapping:** method/path-based registration of an HTTP handler.
- **HttpMessageConverter:** mechanism that reads/writes HTTP body representations such as JSON.

## 60-second explain-it-back
"When I run my main method, SpringApplication prepares a Spring context. Component scanning and conditional auto-configuration register infrastructure and application beans. With the servlet MVC stack, the embedded web server handles HTTP traffic. DispatcherServlet resolves a mapped controller method and uses MVC return-value processing and message converters to create an HTTP response."

This is a teaching-level simplification, not a guarantee of callback ordering.

## Annotation quick-reference
| Annotation | What it does | Doesn't mean |
|---|---|---|
| @SpringBootApplication | Composed application configuration, component scan, auto-config | "This class handles GET" |
| @RestController | Controller whose handler results are response bodies | "Always JSON" |
| @GetMapping | Maps GET to a method/path | "Handles all methods" |
| @RequestParam | Binds request parameters | "Validates every input automatically" |
| @WebMvcTest | MVC slice testing | "Starts a real HTTP server" |

## Practice commands
```powershell
mvn clean test
mvn spring-boot:run
curl.exe -i "http://localhost:8080/api/greetings?name=Alex"
```

## Five questions to self-test (answer without looking)
1. What is Boot doing that Spring Framework alone does not do for you by default?
2. How are IoC and DI related but not identical?
3. How does request reach @GetMapping?
4. Why can 404 happen even if the application started?
5. Does @RestController always serialize to JSON? Why not?

## Common mistake → fix
- `mvn test run` → separate `mvn test` and `mvn spring-boot:run`.
- Singular/plural route mismatch → match @GetMapping exactly.
- Controller outside scan boundary → adjust package structure or explicit configuration.
- Confusing servlet server with MVC dispatcher → separate network/servlet container from framework dispatch logic.

## Next-day recall
Explain all five questions tomorrow without notes. A viewer who can only recognize the answer on screen has not yet mastered it.
