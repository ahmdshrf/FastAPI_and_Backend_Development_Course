# Ultimate Guide to FastAPI and Backend Development

This repository contains code and examples from the O'Reilly course **Ultimate Guide to FastAPI and Backend Development**.

- **Course Link:** [https://learning.oreilly.com/course/ultimate-guide-to/9781806101337/](https://learning.oreilly.com/course/ultimate-guide-to/9781806101337/)
- **Status:** Chapter 7 completed
- **Python:** 3.7+
- **Framework:** FastAPI

## Project Overview

A hands-on learning project for FastAPI and backend development. The app includes a simple API endpoint to practice route creation, request/response schemas, and interactive documentation.

## Features

- FastAPI app scaffold
- SQLite database-backed shipment storage
- CRUD API endpoints for shipments
- Pydantic models for validation
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
  - Returns a shipment by ID.
  - Query param: `id` (int, required)
  - Response: `ShipmentRead` model

- `GET /shipment/latest`
  - Returns the most recent shipment.
  - Response: `ShipmentRead` model

- `POST /shipment`
  - Creates a new shipment.
  - Body: `ShipmentCreate` model (content, weight, destination, zip_code optional)
  - Response: `{ "id": new_id }`

- `PATCH /shipment`
  - Partially updates a shipment.
  - Query param: `id` (int)
  - Body: `ShipmentUpdate` model (all fields optional)
  - Response: Updated `ShipmentRead`

- `DELETE /shipment`
  - Deletes a shipment by ID.
  - Query param: `id` (int)
  - Response: `{ "detail": "Shipment with ID {id} has been deleted" }`

### Data Models

- **ShipmentStatus**: Enum (`pending`, `in_transit`, `delivered`, `placed`, `out_for_delivery`)
- **ShipmentCreate**: `content` (str, max 50), `weight` (float >0 <=25), `destination` (str, max 100), `zip_code` (int, optional)
- **ShipmentRead**: Inherits ShipmentCreate + `shipment_status`
- **ShipmentUpdate**: All fields optional, for partial update

### Example responses

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

## API Documentation

- Swagger: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Project Structure

```
app/
├── __init__.py
├── main.py       # FastAPI app and API endpoints
├── schemas.py    # Pydantic models for request/response validation
└── database.py   # SQLite database logic and persistence
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