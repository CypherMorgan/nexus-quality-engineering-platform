# Nexus Quality Engineering Platform

![Python](https://img.shields.io/badge/python-3.12-blue)
![Playwright](https://img.shields.io/badge/playwright-latest-green)
![Pytest](https://img.shields.io/badge/pytest-framework-orange)
![Docker](https://img.shields.io/badge/docker-enabled-blue)
![GitHub Actions](https://img.shields.io/badge/CI-CD-success-brightgreen)

Enterprise-inspired Quality Engineering platform built using Playwright, PyTest, API Automation, Database Validation, Docker, Allure Reporting, and GitHub Actions.

Designed to demonstrate modern QA Automation engineering practices including UI testing, API validation, database verification, observability, CI/CD integration, accessibility testing, visual validation, and end-to-end workflows.

---

## Features

### UI Automation

* Playwright (Python)
* Page Object Model
* Cross-browser support
* Screenshot capture
* Video recording
* Trace collection
* Network interception

### API Automation

* API client abstraction
* Authentication layer
* Response validation
* JSON schema validation
* Contract testing support

### Database Validation

* SQLite support
* PostgreSQL-ready architecture
* Query abstraction layer
* Database assertions

### Reporting

* Allure Reports
* Failure screenshots
* Environment metadata
* Execution artifacts

### Quality Engineering

* Accessibility testing
* Visual validation
* Mock APIs
* Data-driven testing
* End-to-End validation

### DevOps

* Dockerized execution
* GitHub Actions CI/CD
* Smoke suite
* Regression suite
* Scheduled execution

---

## Architecture

See:

* docs/architecture.md
* docs/execution-flow.md
* docs/cicd.md
* docs/reporting.md

---

## Project Structure

```text
nexus-quality-engineering-platform
├── src/
├── tests/
├── config/
├── sql/
├── app/
├── reports/
├── docs/
├── .github/
└── docker-compose.yml
```

---

## Quick Start

### Local

```bash
pip install -r requirements.txt
playwright install
pytest -v
```

### Docker

```bash
docker compose build
docker compose up
```

### Smoke Suite

```bash
pytest -m smoke
```

### Regression Suite

```bash
pytest -m regression
```

---

## Reporting

Generate Allure Report

```bash
allure serve allure-results
```

---

## CI/CD

### Smoke Pipeline

* Runs on push
* Runs on pull request

### Regression Pipeline

* Manual execution
* Scheduled execution

Artifacts:

* Allure Results
* Reports
* Logs

---

## Test Categories

```bash
pytest -m smoke
pytest -m regression
pytest -m api
pytest -m ui
pytest -m database
pytest -m e2e
pytest -m accessibility
pytest -m visual
```

---

## Future Enhancements

* PostgreSQL service container
* Kubernetes execution
* BrowserStack integration
* Pact contract testing
* Grafana dashboards
* OpenTelemetry integration

---

## Author

Built as a portfolio project demonstrating modern QA Automation and Quality Engineering practices using Python, Playwright, Docker, and CI/CD.
