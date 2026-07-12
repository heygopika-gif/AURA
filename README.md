# Project Aura

Project Aura is a personalized AI life coach designed to help users manage goals, habits, journals, and long-term personal growth through intelligent conversations and memory. Rather than functioning as a simple chatbot, Aura is being built as a data platform with a conversational interface, where persistent memory and structured data enable personalized guidance over time.

## Architecture

The project follows a modular architecture that separates responsibilities into independent layers. Configuration is managed through typed settings, the API layer handles HTTP requests, the service layer contains business logic, repositories manage data access, and the database stores long-term user information. This structure keeps the application maintainable, testable, and scalable as new features are added.

## Tech Stack

* Python 3.12
* FastAPI
* Pydantic Settings
* SQLAlchemy
* Alembic
* SQLite (development)
* Uvicorn

## Getting Started

### Prerequisites

* Python 3.12
* uv package manager

### Installation

```bash
uv sync
```

### Running the application

```bash
uv run uvicorn app.main:create_app --factory --reload
```

After the server starts, open:

* http://127.0.0.1:8000/docs

## Project Status

Project Aura is currently under active development. The project is being built incrementally with a focus on clean architecture, dependency injection, testing, and long-term maintainability.

## Documentation

Additional design decisions and architecture documentation will be maintained in the project's documentation as development progresses.
