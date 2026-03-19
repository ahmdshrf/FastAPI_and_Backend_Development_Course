# Ultimate Guide to FastAPI and Backend Development

This repository contains code and examples from the O'Reilly course **Ultimate Guide to FastAPI and Backend Development**.

**Course Link:** [https://learning.oreilly.com/course/ultimate-guide-to/9781806101337/](https://learning.oreilly.com/course/ultimate-guide-to/9781806101337/)

**Status:** In Progress

## Project Overview

This project demonstrates building backend APIs using FastAPI, a modern, fast web framework for building APIs with Python 3.7+ based on standard Python type hints.

## Features

- Basic FastAPI application setup
- RESTful API endpoints
- JSON response handling

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd FastAPI_and_Backend_Development_Course
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:
   ```bash
   pip install fastapi uvicorn
   ```

## Running the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

## API Endpoints

### GET /shipment

Returns shipment details.

**Response:**
```json
{
  "content": "wooden table",
  "weight": 100,
  "destination": "New York"
}
```

## Interactive API Documentation

Once the server is running, visit `http://127.0.0.1:8000/docs` for the interactive Swagger UI documentation.

## Project Structure

```
app/
├── __init__.py
└── main.py          # Main FastAPI application
```

## Contributing

This is a learning project for the O'Reilly course. Feel free to explore and modify the code as you follow along with the course content.

## License

This project is for educational purposes as part of the O'Reilly course.