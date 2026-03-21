# Ultimate Guide to FastAPI and Backend Development

This repository contains code and examples from the O'Reilly course **Ultimate Guide to FastAPI and Backend Development**.

- **Course Link:** [https://learning.oreilly.com/course/ultimate-guide-to/9781806101337/](https://learning.oreilly.com/course/ultimate-guide-to/9781806101337/)
- **Status:** Chapter 5 complete (continuing through Chapter 6)
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
  - Returns the latest shipment or a specific shipment by ID.
  - Query param: `id` (optional, int)

- `GET /shipment/latest`
  - Returns the most recent shipment.

- `POST /shipment`
  - Creates a new shipment.
  - Query params: `weight` (float), `destination` (str)
  - Body: `{"content": "string"}`
  - New shipment default `shipment_status` set to `pending`

- `PUT /shipment`
  - Updates an existing shipment fully by ID.
  - Body/query params: `id` (int), `content` (str), `weight` (float), `destination` (str), `shipment_status` (str)

- `PATCH /shipment`
  - Partially updates shipment fields.
  - Body: partial update object (e.g., `{"weight": 1.0, "shipment_status":"delivered"}`)

- `DELETE /shipment`
  - Deletes a shipment by ID.
  - Query param: `id` (int)

- `GET /shipments/{field}`
  - Returns a specific field from a shipment.
  - Path param: `field` (str, e.g., "content", "weight", "destination", "shipment_status")
  - Query param: `id` (int)

### Example responses

**GET /shipment** (latest):
```json
{
  "content": "sofa",
  "weight": 4.1,
  "destination": "Vienna"
}
```

**POST /shipment** (response):
```json
{
  "id": 12085
}
```

**GET /shipments/content?id=12078**:
```
"table"
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