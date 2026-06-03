# CI/CD Pipeline

```mermaid
graph TD

A[Developer Push]

A --> B[GitHub Actions]

B --> C[Build]

C --> D[Smoke Suite]

D --> E[Regression Suite]

E --> F[Artifacts]

F --> G[Allure Results]
```
