from typing import Any
from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference
from .schemas import ShipmentCreate, ShipmentRead , ShipmentStatus, ShipmentUpdate #you can also import Shipment from app.schemas if you want to run the code outside of the app directory
from .database import Database
app = FastAPI()

db = Database()
# shipments = {
#     12078: {
#         "content": "table",
#         "weight": 0.78,
#         "destination": "Paris",
#         "shipment_status": "in_transit",
#         "zip_code": 75001,
#     },
#     12079: {
#         "content": "chair",
#         "weight": 0.5,
#         "destination": "London",
#         "shipment_status": "delivered",
#         "zip_code": 12345,
#     },
#     12080: {
#         "content": "bookshelf",
#         "weight": 2.3,
#         "destination": "Berlin",
#         "shipment_status": "pending",
#         "zip_code": 10117,
#     },
#     12081: {
#         "content": "lamp",
#         "weight": 0.8,
#         "destination": "Rome",
#         "shipment_status": "in_transit",
#         "zip_code": 100,
#     },
#     12082: {
#         "content": "desk",
#         "weight": 1.5,
#         "destination": "Madrid",
#         "shipment_status": "pending",
#         "zip_code": 28001,
#     },
#     12083: {
#         "content": "cabinet",
#         "weight": 3.2,
#         "destination": "Amsterdam",
#         "shipment_status": "delivered",
#         "zip_code": 1012,
#     },
#     12084: {
#         "content": "sofa",
#         "weight": 4.1,
#         "destination": "Vienna",
#         "shipment_status": "in_transit",
#         "zip_code": 1010,
#     },
# }


@app.get("/shipment/latest", response_model=ShipmentRead)
def get_shipment_latest() -> dict[str, Any] | None:
    latest_shipment = db.get_latest_shipment()
    if latest_shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Givern ID not found"
        )
    return latest_shipment

@app.get("/shipment", response_model=ShipmentRead)
def get_shipment(id: int) -> dict[str, Any] :
    shipment = db.get_shipment(id)
    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Givern ID not found"
        )
    return shipment




@app.post("/shipment")
def create_shipment(
    body: ShipmentCreate
) -> dict[str, int]:
    new_id = db.create_shipment(body)
    return {
        "id": new_id
    }


@app.patch("/shipment", response_model=ShipmentRead)
def update_shipment(
    id: int,
    body: ShipmentUpdate
) -> dict[str, Any]:
    update_shipment = db.update_shipment(id, body)
    return update_shipment

@app.delete("/shipment")
def delete_shipment(id: int) -> dict[str, Any]:
    db.delete_shipment(id)
    return {"detail": f"Shipment with ID {id} has been deleted"}

# @app.get("/shipments/{field}")
# def get_shipments_fields(field: str, id: int) -> Any:
#     return shipments[id][field]


@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="Scalar API ")
