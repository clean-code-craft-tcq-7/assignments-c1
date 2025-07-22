# Course transcripts

This page covers the concepts covered in the exercises

## Purpose

Build habits for productivity and reliability.

```mermaid
graph LR
    subgraph Productivity
        A1["Quick releases"]
        A2["More features"]
        A3["Smaller teams"]
        A4["Deadlines"]
        A[Productivity]
        A1 --> A
        A2 --> A
        A3 --> A
        A4 --> A
    end

    subgraph Reliability
        B1["Test coverage"]
        B2["Linters"]
        B3["Modularity"]
        B4["Graceful degradation"]
        B[Reliability]
        B1 --> B
        B2 --> B
        B3 --> B
        B4 --> B
    end

    C["Productivity AND Reliability"]
    A --> C
    B --> C
```

## Tests

Follow the FIRST principles for writing tests:

| Principle | Enables | Benefits |
|-----------|---------|----------|
| Fast      | Frequent execution | Find issues early |
| Independent| Isolation of tests | Easier failure diagnosis |
| Repeatable | Consistent results | Stable tests, low maintenance |
| Self-validating| Automatic pass/fail | Reduced manual effort - single Pass/Fail result |
| Thorough   | Coverage with strong asserts | Passing tests ensure customer satisfaction |
