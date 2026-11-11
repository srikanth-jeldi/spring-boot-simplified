package com.springbootsimplified.day01;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class GreetingController {
    @GetMapping("/api/greetings")
    public Greeting greeting(@RequestParam(defaultValue = "Developer") String name) {
        return new Greeting("Hello, " + name + "!", "Spring Boot Simplified");
    }

    public record Greeting(String message, String course) {}
}
