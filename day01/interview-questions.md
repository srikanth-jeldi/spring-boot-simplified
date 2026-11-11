# Day 01 — Interview Questions and Tricky Answers

**Q1. Does Spring Boot replace Spring Framework?** No. Boot builds on Spring and adds conditional auto-configuration, dependency management conventions, and operational features.

**Q2. Will a starter always create every bean?** No. Auto-configurations have conditions on classpath, properties, beans, and application type.

**Q3. Is `@SpringBootApplication` equivalent to `@RestController`?** No. The former bootstraps configuration, scanning and auto-configuration; the latter declares an HTTP controller.

**Q4. Why is a controller not detected?** Component scanning defaults to the main application package and its subpackages. Unrelated packages may not be scanned.

**Q5. Is Tomcat the same as `DispatcherServlet`?** No. Tomcat accepts servlet HTTP traffic; DispatcherServlet is Spring MVC's front controller for mapped handlers.

**Q6. Does Spring Boot always use Tomcat?** No. The MVC servlet starter normally brings embedded Tomcat by default, but servers and reactive stacks can differ.

**Q7. What does `SpringApplication.run()` return?** A `ConfigurableApplicationContext`.

**Q8. Will `@GetMapping` work after removing the web starter?** Not necessarily. You may lose classes at compile time or the required web runtime.

**Q9. Why can an application start but still return 404?** The requested route may be incorrect, the controller may not be registered, or context-path/mapping configuration may differ.

**Q10. Does `@RestController` force JSON for every return value?** No. Return-value processing, available message converters and content negotiation determine representation; a `String` return often becomes text.

**Q11. What if port 8080 is busy?** The embedded server generally fails to bind. Stop the other process or configure `server.port`.

**Q12. Is auto-configuration 'magic'?** No. It is condition-driven configuration backed by ordinary Spring beans and application lifecycle.

## Senior-level scenario
*Question:* A controller works in local tests but not after moving it into a new module. What do you check first?

*Answer:* Compare package structure and component-scanning boundaries, application startup logs and registered handler mappings. Verify dependency packaging and test the URL. Don't immediately add `@ComponentScan` globally without determining the root cause.
