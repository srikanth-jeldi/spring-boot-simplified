# 30-day Spring Boot Simplified curriculum

Goal: ~90 original lessons, adjusted for complexity rather than forcing one concept into a fixed runtime. Every core module combines concepts, runnable coding, failure experiments, real production problems, and interview traps.

| Day | Concept | Build | Advanced / Tricky |
|---|---|---|---|
| 01 | What is Spring Boot? | First API | Spring vs Boot |
| 02 | Inversion of Control | Managed beans | IoC lifecycle |
| 03 | Dependency Injection | Constructor injection | Field injection traps |
| 04 | Bean lifecycle | Hooks and scopes | Singleton concurrency |
| 05 | Auto-configuration | Starter and properties | Conditional beans |
| 06 | Component annotations | Bean registration | Stereotypes vs @Bean |
| 07 | Layered architecture | Service & repository | Boundaries |
| 08 | REST fundamentals | CRUD APIs | PUT vs PATCH |
| 09 | Spring MVC internals | HTTP parameters | DispatcherServlet |
| 10 | Validation | Constraints | Group validation |
| 11 | Error handling | Problem responses | Global advice |
| 12 | Spring Data JPA | CRUD persistence | ORM behavior |
| 13 | Entity relationships | Associations | N+1 queries |
| 14 | Transactions | Flyway & rollback | Proxy self-invocation |
| 15 | Spring Security | Filter chain | AuthN vs AuthZ |
| 16 | JWT | Login and protected API | Token pitfalls |
| 17 | OAuth2/OIDC | Resource server | Token models |
| 18 | Unit testing | JUnit & Mockito | Mock boundaries |
| 19 | Integration testing | MockMvc & Testcontainers | Test isolation |
| 20 | Profiles & config | Secrets/config | Environment leakage |
| 21 | Observability | Actuator & logs | Production debugging |
| 22 | Microservices | Service split | When not to split |
| 23 | Service discovery | Eureka | Discovery alternatives |
| 24 | API gateway | Routing & filters | Trust boundaries |
| 25 | HTTP clients | Timeouts & retries | Idempotency |
| 26 | Resilience | Circuit breakers | Retry storms |
| 27 | Event-driven systems | Kafka basics | Delivery semantics |
| 28 | Redis cache | Cache-aside | Invalidation |
| 29 | Containerization | Docker image | Config at runtime |
| 30 | Deployment overview | Run & monitor | Architecture review |

## Scope honesty
Thirty days builds a strong foundation, **not** complete architect-level mastery. Kafka, Kubernetes, AWS, distributed transactions and performance engineering merit separate, deeper series.

## Repository quality gate
Every coding lesson: `mvn test` passes, output is reproduced, dependencies are pinned, known caveats documented. A lesson is **draft** until these checks succeed.
