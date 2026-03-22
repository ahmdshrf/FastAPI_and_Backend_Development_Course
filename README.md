# Ultimate Guide to FastAPI and Backend Development

This repository contains code and examples from the O'Reilly course **Ultimate Guide to FastAPI and Backend Development**.

- **Course Link:** [https://learning.oreilly.com/course/ultimate-guide-to/9781806101337/](https://learning.oreilly.com/course/ultimate-guide-to/9781806101337/)
- **Status:** Chapter 6 completed
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
  - Response: `ShipmentRead` model

- `GET /shipment/latest`
  - Returns the most recent shipment with ID.
  - Response: JSON with `id`, `content`, `weight`, `destination`, `shipment_status`, `zip_code`

- `POST /shipment`
  - Creates a new shipment.
  - Body: `ShipmentCreate` model (content, weight, destination, zip_code optional)
  - Response: `{"id": new_id}`

- `PUT /shipment`
  - Updates an entire shipment.
  - Query param: `id` (int)
  - Body: `ShipmentRead` model
  - Response: Updated `ShipmentRead`

- `PATCH /shipment`
  - Partially updates a shipment.
  - Query param: `id` (int)
  - Body: `ShipmentUpdate` model (optional fields)
  - Response: Updated `ShipmentRead`

- `DELETE /shipment`
  - Deletes a shipment by ID.
  - Query param: `id` (int)
  - Response: `{"detail": "Shipment with ID {id} has been deleted"}`

- `GET /shipments/{field}`
  - Returns a specific field from a shipment.
  - Path param: `field` (str, e.g., "content", "weight", "destination", "shipment_status", "zip_code")
  - Query param: `id` (int)
  - Response: Field value

### Data Models

- **ShipmentStatus**: Enum (`pending`, `in_transit`, `delivered`, `placed`)
- **ShipmentCreate**: `content` (str, max 50), `weight` (float >0 <=25), `destination` (str, max 100), `zip_code` (int, optional)
- **ShipmentRead**: Inherits ShipmentCreate + `shipment_status`
- **ShipmentUpdate**: Optional fields from ShipmentRead

### Example responses

**GET /shipment** (latest):
```json
{
  "content": "sofa",
  "weight": 4.1,
  "destination": "Vienna",
  "zip_code": 1010,
  "shipment_status": "in_transit"
}
```

**GET /shipment/latest**:
```json
{
  "id": 12084,
  "content": "sofa",
  "weight": 4.1,
  "destination": "Vienna",
  "shipment_status": "in_transit",
  "zip_code": 1010
}
```

**POST /shipment** (request body):
```json
{
  "content": "books",
  "weight": 1.2,
  "destination": "Tokyo"
}
```
Response:
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
├── main.py       # main FastAPI app implementation
└── schemas.py    # Pydantic models for request/response validation
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