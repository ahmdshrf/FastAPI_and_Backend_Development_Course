from typing import Any
from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference
from .schemas import ShipmentCreate, ShipmentRead , ShipmentStatus, ShipmentUpdate #you can also import Shipment from app.schemas if you want to run the code outside of the app directory
app = FastAPI()

shipments = {
    12078: {
        "content": "table",
        "weight": 0.78,
        "destination": "Paris",
        "shipment_status": "in_transit",
        "zip_code": 75001,
    },
    12079: {
        "content": "chair",
        "weight": 0.5,
        "destination": "London",
        "shipment_status": "delivered",
        "zip_code": 12345,
    },
    12080: {
        "content": "bookshelf",
        "weight": 2.3,
        "destination": "Berlin",
        "shipment_status": "pending",
        "zip_code": 10117,
    },
    12081: {
        "content": "lamp",
        "weight": 0.8,
        "destination": "Rome",
        "shipment_status": "in_transit",
        "zip_code": 100,
    },
    12082: {
        "content": "desk",
        "weight": 1.5,
        "destination": "Madrid",
        "shipment_status": "pending",
        "zip_code": 28001,
    },
    12083: {
        "content": "cabinet",
        "weight": 3.2,
        "destination": "Amsterdam",
        "shipment_status": "delivered",
        "zip_code": 1012,
    },
    12084: {
        "content": "sofa",
        "weight": 4.1,
        "destination": "Vienna",
        "shipment_status": "in_transit",
        "zip_code": 1010,
    },
}


@app.get("/shipment/latest")
def get_shipment_latest():
    latest_id = max(shipments.keys())
    return {
        "id": latest_id,
        "content": shipments[latest_id]["content"],
        "weight": shipments[latest_id]["weight"],
        "destination": shipments[latest_id]["destination"],
        "shipment_status": shipments[latest_id]["shipment_status"],
        "zip_code": shipments[latest_id]["zip_code"],
    }


@app.get("/shipment", response_model=ShipmentRead)
def get_shipment(id: int | None = None) :

    if id is None:
        return shipments[max(shipments.keys())]
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Givern ID not found"
        )
    return shipments[id]


@app.post("/shipment")
def create_shipment(
    body: ShipmentCreate
) -> dict[str, int]:
    new_id = max(shipments.keys()) + 1
    shipments[new_id] = {
        **body.model_dump(),
        "shipment_status": ShipmentStatus.PLACED,
    }
    return {
        "id": new_id,
    }


@app.put("/shipment", response_model=ShipmentRead)
def update_shipment(
    id: int,
    shipment: ShipmentRead
) -> dict[str, Any]:
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Given ID not found"
        )
    weight = shipment.weight
    content = shipment.content
    destination = shipment.destination
    shipment_status = shipment.shipment_status
    zip_code = shipment.zip_code
    
    shipments[id] = {
        "content": content,
        "weight": weight,
        "destination": destination,
        "shipment_status": shipment_status,
        "zip_code": zip_code,
    }
    return shipments[id]

@app.patch("/shipment", response_model=ShipmentRead)
def patch_shipment(
    id: int,
    body: ShipmentUpdate
) -> dict[str, Any]:
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Given ID not found"
        )
    body_dict = body.model_dump(exclude_none=True)
    shipments[id].update(body_dict)
    # if weight :
    #     shipments[id]["weight"] = weight
    # if content :
    #     shipments[id]["content"] = content
    # if destination :
    #     shipments[id]["destination"] = destination
    # if shipment_status :
    #     shipments[id]["shipment_status"] = shipment_status
    return shipments[id]

@app.delete("/shipment")
def delete_shipment(id: int) -> dict[str, Any]:
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Given ID not found"
        )
    shipments.pop(id)
    return {"detailed": f"Shipment with ID {id} has been deleted"}

@app.get("/shipments/{field}")
def get_shipments_fields(field: str, id: int) -> Any:
    return shipments[id][field]


@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="Scalar API ")
