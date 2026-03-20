# Ultimate Guide to FastAPI and Backend Development

This repository contains code and examples from the O'Reilly course **Ultimate Guide to FastAPI and Backend Development**.

- **Course Link:** [https://learning.oreilly.com/course/ultimate-guide-to/9781806101337/](https://learning.oreilly.com/course/ultimate-guide-to/9781806101337/)
- **Status:** In Progress
- **Python:** 3.7+
- **Framework:** FastAPI

## Project Overview

A hands-on learning project for FastAPI and backend development. The app includes a simple API endpoint to practice route creation, request/response schemas, and interactive documentation.

## Features

- FastAPI app scaffold
- JSON-based REST endpoint
- FastAPI dev server with auto-reload
- Swagger UI and ReDoc docs

## Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)

## Installation

1. Clone repository:
   ```bash
   git clone https://github.com/<your-account>/FastAPI_and_Backend_Development_Course.git
   cd FastAPI_and_Backend_Development_Course
   ```

2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate   # Windows
   source venv/bin/activate    # macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install fastapi
   ```

## Run the Application

```bash
fastapi dev
```

Open `http://127.0.0.1:8000` in your browser.

## API Endpoints

- `GET /shipment`
  - Returns a sample shipment object.

### Example response

```json
{
  "content": "wooden table",
  "weight": 100,
  "destination": "New York"
}
```

## API Documentation

- Swagger: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Project Structure

```
app/
├── __init__.py
└── main.py       # main FastAPI app implementation
```

## Development Notes

- Update `app/main.py` to add new endpoints and route logic.
- Use `pydantic` models in future enhancements for request/response validation.

## Contributing

1. Fork the repository
2. Create branch `feature/<name>`
3. Add or update endpoints and tests
4. Open Pull Request

## License

Educational use only for O'Reilly course practice.