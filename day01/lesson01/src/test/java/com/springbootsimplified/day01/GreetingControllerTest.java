package com.springbootsimplified.day01;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.webmvc.test.autoconfigure.WebMvcTest;
import org.springframework.test.web.servlet.MockMvc;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@WebMvcTest(GreetingController.class)
class GreetingControllerTest {
    @Autowired MockMvc mvc;

    @Test void returnsDefaultGreeting() throws Exception {
        mvc.perform(get("/api/greetings"))
           .andExpect(status().isOk())
           .andExpect(jsonPath("$.message").value("Hello, Developer!"));
    }

    @Test void returnsCustomGreeting() throws Exception {
        mvc.perform(get("/api/greetings").param("name", "Alex"))
           .andExpect(status().isOk())
           .andExpect(jsonPath("$.message").value("Hello, Alex!"))
           .andExpect(jsonPath("$.course").value("Spring Boot Simplified"));
    }
}
