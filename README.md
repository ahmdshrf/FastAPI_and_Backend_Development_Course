# Ultimate Guide to FastAPI and Backend Development

This repository contains code and examples from the O'Reilly course **Ultimate Guide to FastAPI and Backend Development**.

- **Course Link:** [https://learning.oreilly.com/course/ultimate-guide-to/9781806101337/](https://learning.oreilly.com/course/ultimate-guide-to/9781806101337/)
- **Status:** Chapter 8 completed
- **Python:** 3.7+
- **Framework:** FastAPI
- **Database:** SQLite with SQLModel ORM

## 📋 Project Overview

A hands-on learning project for FastAPI and backend development. This application provides a complete shipment management system with REST API endpoints, demonstrating best practices for route creation, request/response validation, database integration, and interactive API documentation.

## ✨ Features

- ⚡ FastAPI app with async support
- 🗄️ SQLite database with SQLModel ORM
- 📦 Complete CRUD operations for shipment management
- ✅ Pydantic models for request/response validation
- 🔄 Automatic database table creation on startup
- 📚 Interactive Swagger UI and ReDoc documentation
- 🔌 Scalar API reference support
- 🔄 Auto-reload development server

## 📋 Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)
- Virtual environment (recommended)

## 🚀 Installation

### 1. Clone the repository
```bash
git clone https://github.com/<your-account>/FastAPI_and_Backend_Development_Course.git
cd FastAPI_and_Backend_Development_Course
```

### 2. Create and activate virtual environment

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install fastapi uvicorn sqlmodel sqlalchemy
```

Or install from requirements file (if available):
```bash
pip install -r requirements.txt
```

## ▶️ Run the Application

Start the FastAPI development server:
```bash
fastapi dev
```

Or using uvicorn directly:
```bash
uvicorn app.main:app --reload
```

The application will be available at:
- **API**: http://127.0.0.1:8000
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc
- **Scalar API Reference**: http://127.0.0.1:8000/scalar

## � API Documentation

This project uses **Scalar** as the primary API documentation tool, alongside traditional Swagger UI and ReDoc options.

### Scalar Documentation
**Scalar** is a modern, beautiful alternative to Swagger UI that provides:
- 🎨 Clean, modern user interface
- 📱 Responsive design optimized for desktop and mobile
- 🔍 Advanced search and filtering
- 💾 Request history and examples
- 🧪 Built-in API testing capabilities
- 📖 Better readability for complex API schemas

**Access Scalar**: http://127.0.0.1:8000/scalar

The Scalar documentation is integrated via the `scalar_fastapi` package and provides an intuitive way to explore and test all available endpoints.

### Alternative Documentation
- **Swagger UI** (Traditional): http://127.0.0.1:8000/docs
- **ReDoc** (Alternative UI): http://127.0.0.1:8000/redoc

All documentation formats display the same API schema and are automatically generated from the FastAPI application code.

## �📁 Project Structure

```
FastAPI_and_Backend_Development_Course/
├── app/
│   ├── __init__.py               # App package initialization
│   ├── main.py                   # FastAPI application and route handlers
│   ├── schemas.py                # Pydantic/SQLModel models
│   ├── database.py               # Legacy database utility class
│   └── database/
│       ├── __init__.py
│       ├── models.py             # SQLModel database models
│       └── session.py            # SQLAlchemy session management
├── venv/                         # Virtual environment
├── test.py                       # Test script
├── README.md                     # This file
└── sqlite.db                     # SQLite database (generated on first run)
```

## 📊 Data Models

### ShipmentStatus Enum
Available status values:
- `pending` - Shipment awaiting dispatch
- `in_transit` - Shipment is on the way
- `delivered` - Shipment has been delivered
- `placed` - Order has been placed
- `out_for_delivery` - Shipment is out for delivery

### BaseShipment Model
Base model with core shipment fields:
- `content` (str, max 50 chars) - Description of shipment content
- `weight` (float) - Weight in kg (must be > 0 and ≤ 25)
- `destination` (str, max 100 chars) - Delivery destination
- `zip_code` (int, optional) - Postal code (auto-generated if not provided)

### Shipment Model
Complete database model inheriting from BaseShipment:
- `id` (int) - Primary key
- `shipment_status` (ShipmentStatus) - Current status
- `estimated_delivery` (datetime) - Estimated delivery date

### ShipmentCreate Model
Used for POST requests (inherits from BaseShipment)

### ShipmentUpdate Model
Used for PATCH requests (all fields optional):
- `shipment_status` (ShipmentStatus, optional)
- `estimated_delivery` (datetime, optional)

## 🔌 API Endpoints

### Get Shipment by ID
```http
GET /shipment?id=1
```
**Parameters:**
- `id` (query, required) - Shipment ID

**Response (200):**
```json
{
  "id": 1,
  "content": "laptop",
  "weight": 2.5,
  "destination": "New York",
  "zip_code": 10001,
  "shipment_status": "in_transit",
  "estimated_delivery": "2026-04-10T15:30:00"
}
```

### Get Latest Shipment
```http
GET /shipment/latest
```
**Response (200):**
```json
{
  "id": 5,
  "content": "sofa",
  "weight": 4.1,
  "destination": "Vienna",
  "zip_code": 1010,
  "shipment_status": "in_transit",
  "estimated_delivery": "2026-04-12T10:00:00"
}
```

### Create New Shipment
```http
POST /shipment
```
**Request Body:**
```json
{
  "content": "monitor",
  "weight": 3.5,
  "destination": "London",
  "zip_code": 12345
}
```

**Response (201):**
```json
{
  "id": 6
}
```

### Update Shipment
```http
PATCH /shipment?id=1
```
**Parameters:**
- `id` (query, required) - Shipment ID to update

**Request Body:**
```json
{
  "shipment_status": "delivered",
  "estimated_delivery": "2026-04-08T14:00:00"
}
```

**Response (200):**
```json
{
  "id": 1,
  "content": "laptop",
  "weight": 2.5,
  "destination": "New York",
  "zip_code": 10001,
  "shipment_status": "delivered",
  "estimated_delivery": "2026-04-08T14:00:00"
}
```

### Delete Shipment
```http
DELETE /shipment?id=1
```
**Parameters:**
- `id` (query, required) - Shipment ID to delete

**Response (200):**
```json
{
  "detail": "Shipment with ID 1 has been deleted"
}
```

## 🗄️ Database

The application uses SQLite with SQLModel ORM. The database is automatically created on first run with the required `shipment` table.

**Database file:** `sqlite.db` (created in project root)

### Database Schema
```sql
CREATE TABLE IF NOT EXISTS shipment (
  id INTEGER PRIMARY KEY,
  content TEXT NOT NULL,
  weight REAL NOT NULL,
  destination TEXT NOT NULL,
  shipment_status TEXT NOT NULL,
  zip_code INTEGER,
  estimated_delivery DATETIME NOT NULL
)
```

## 🛠️ Development

### Hot Reload
Changes to code files automatically reload the server when using `fastapi dev` or `uvicorn` with `--reload` flag.

### Testing
Run the test file:
```bash
python test.py
```

### Dependencies
- **fastapi** - Web framework
- **uvicorn** - ASGI server
- **sqlmodel** - SQL ORM combining SQLAlchemy + Pydantic
- **sqlalchemy** - Database toolkit
- **scalar-fastapi** - Modern API documentation

## 📝 License

This is a learning project based on the O'Reilly course. Follow the course terms for usage.

## 🤝 Contributing

This is a learning repository. Feel free to fork and experiment!
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