# Day 01 — Spring Boot Fundamentals

## Learning goals
- Explain Spring Framework vs Spring Boot accurately.
- Understand what `@SpringBootApplication` does (configuration, component scanning, auto-configuration).
- Trace an HTTP request from embedded server through Spring MVC to a controller.
- Build, run and test a small endpoint.
- Diagnose a `404 Not Found` due to an incorrect URL or missing controller scan.

## Real-world analogy
For an online food-ordering system, Spring Framework provides foundational components for wiring services and serving HTTP requests. Spring Boot adds auto-configuration, curated dependencies and conventions so you spend less time on wiring. It does **not** remove the need to understand Spring.

## Request X-Ray
```text
HTTP client → embedded servlet server (typically Tomcat)
            → servlet filter chain
            → DispatcherServlet
            → handler mapping → GreetingController
            → return value / HttpMessageConverter
            → HTTP response
```
This is a simplified flow. In production, authentication, interceptors, error handling and more may participate.

## Run it
```powershell
cd day01/lesson01
mvn test
mvn spring-boot:run
Invoke-RestMethod "http://localhost:8080/api/greetings?name=Alex"
```

## Break → Fix
Change the request to `/api/greeting` (singular). Expect 404, because the controller maps `/api/greetings`. Correct the URL. Next move the controller outside the root package and discuss component scanning before restoring it.

## Practice
1. Add `/api/health-message` returning a JSON record.
2. Write one MVC slice test.
3. Explain why a controller under an unrelated package might not be registered.

See [Q&A](interview-questions.md).
