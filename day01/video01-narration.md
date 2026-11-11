# Day 01 / Video 01 — Narration and Visual Storyboard

**Proposed title:** What Is Spring Boot? See What Happens Inside Your First API
**Audience:** beginner through experienced Java developer
**Voice candidate:** Kokoro am_michael; approval pending
**Status:** script/storyboard ready; final mastered voice and video NOT rendered

## 01 — Hook: Build a food-ordering backend
**Narration:** "Imagine you're building an ordering application. You need HTTP endpoints, configuration, a server, and a reliable way to connect components. Which pieces should you wire manually—and which ones can the framework prepare?"
**Visual:** Order app cards: HTTP / server / configuration / business logic.

## 02 — Framework vs Boot
**Narration:** "Spring Framework supplies the core programming model: beans, dependency injection, and web MVC. Spring Boot builds on top. It chooses useful defaults, configures components conditionally, and gives you a straightforward way to run the application."
**Visual:** Show Spring foundation, then Boot configuration layer; avoid claiming they are competing frameworks.

## 03 — `@SpringBootApplication`
**Narration:** "This annotation combines configuration, component scanning, and enabling auto-configuration. It doesn't process HTTP requests by itself."
**Visual:** Three expanding sections with corresponding annotations.

## 04 — Classpath and conditional configuration
**Narration:** "Boot examines what's available on the classpath and your configuration. If Spring MVC and a servlet server are present, it can prepare the web application infrastructure. Conditions also allow user-provided configuration to take precedence in many cases."
**Visual:** Classpath + properties → conditions → configuration.

## 05 — The request X-Ray
**Narration:** "A client sends a request. The embedded servlet container accepts it. Spring MVC's DispatcherServlet finds an appropriate controller handler. The return value is written into the HTTP response using the configured converters."
**Visual:** Moving packet through server, servlet, controller and JSON return.

## 06 — Actual code
**Narration:** "Our controller maps GET slash API slash greetings. The name query parameter has a default value. We return a Java record, which can be serialized to JSON when the JSON converter is present."
**Visual:** Highlight `@GetMapping`, `@RequestParam`, record.

## 07 — Break it
**Narration:** "Now request slash API slash greeting—without the final s. The application may be healthy, but that route doesn't exist. We get HTTP 404."
**Visual:** Red 404 and mismatched route; do not simulate a server crash.

## 08 — Fix it
**Narration:** "Use the mapped route, or deliberately change the mapping and its tests. Never respond to every 404 by changing random server settings."
**Visual:** URL comparison and passing test.

## 09 — Interview trap
**Narration:** "Does Spring Boot automatically turn everything into JSON? Not exactly. Response type, converters, and content negotiation matter. An ordinary String response can be plain text."
**Visual:** side-by-side record → JSON; String → text.

## 10 — Recap and challenge
**Narration:** "Spring supplies the framework. Boot simplifies the setup. The server handles network traffic; Spring MVC dispatches the request. Your challenge: add a second endpoint, test it, then explain why it works."
**Visual:** final pipeline + small challenge.

## Technical review requirements
- Keep Maven/Boot version explicit.
- Verify compilation and tests before publishing.
- Make all animated labels legible on mobile.
- Don't present any unexecuted output as captured runtime evidence.
