# Reporting Flow

```mermaid
graph TD

A[Test Failure]

A --> B[Screenshot]

A --> C[Logs]

A --> D[Video]

A --> E[Trace]

B --> F[Allure]
C --> F
D --> F
E --> F

F --> G[Report]
```
