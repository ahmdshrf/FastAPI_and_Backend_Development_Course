from typing import Any
from fastapi import FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference

app = FastAPI()

shipments = {
    12078: {
        "content": "table",
        "weight": 0.78,
        "destination": "Paris",
        "shipment_status": "in_transit",
    },
    12079: {
        "content": "chair",
        "weight": 0.5,
        "destination": "London",
        "shipment_status": "delivered",
    },
    12080: {
        "content": "bookshelf",
        "weight": 2.3,
        "destination": "Berlin",
        "shipment_status": "pending",
    },
    12081: {
        "content": "lamp",
        "weight": 0.8,
        "destination": "Rome",
        "shipment_status": "in_transit",
    },
    12082: {
        "content": "desk",
        "weight": 1.5,
        "destination": "Madrid",
        "shipment_status": "pending",
    },
    12083: {
        "content": "cabinet",
        "weight": 3.2,
        "destination": "Amsterdam",
        "shipment_status": "delivered",
    },
    12084: {
        "content": "sofa",
        "weight": 4.1,
        "destination": "Vienna",
        "shipment_status": "in_transit",
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
    }


@app.get("/shipment")
def get_shipment(id: int | None = None) -> dict[str, Any]:

    if id is None:
        return shipments[max(shipments.keys())]
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Givern ID not found"
        )
    return shipments[id]


@app.post("/shipment")
def create_shipment(
    weight: float, destination: str, data: dict[str, Any]
) -> dict[str, Any]:
    new_id = max(shipments.keys()) + 1
    content = data["content"]

    if weight <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Weight must be a positive number",
        )

    if weight > 100:
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail="Weight must not exceed 100 kg",
        )
    shipments[new_id] = {
        "content": content,
        "weight": weight,
        "destination": destination,
        "shipment_status": "pending",
    }
    return {
        "id": new_id,
    }


@app.put("/shipment")
def update_shipment(
    id: int,
    content: str ,
    weight: float ,
    destination: str ,
    shipment_status: str 
) -> dict[str, Any]:
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Given ID not found"
        )
    if weight is not None:
        if weight <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Weight must be a positive number",
            )
        if weight > 100:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail="Weight must not exceed 100 kg",
            )
        shipments[id] = {
            "content": content,
            "weight": weight,
            "destination": destination,
            "shipment_status": shipment_status,
        }
    return shipments[id]

@app.patch("/shipment")
def patch_shipment(
    id: int,
    content: str | None = None,
    weight: float | None = None,
    destination: str | None = None,
    shipment_status: str | None = None,
) -> dict[str, Any]:
    if id not in shipments:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Given ID not found"
        )
    if weight is not None:
        if weight <= 0:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Weight must be a positive number",
            )
        if weight > 100:
            raise HTTPException(
                status_code=status.HTTP_406_NOT_ACCEPTABLE,
                detail="Weight must not exceed 100 kg",
            )
        shipments[id]["weight"] = weight
    if content :
        shipments[id]["content"] = content
    if destination :
        shipments[id]["destination"] = destination
    if shipment_status :
        shipments[id]["shipment_status"] = shipment_status
    return shipments[id]

@app.get("/shipments/{field}")
def get_shipments_fields(field: str, id: int) -> Any:
    return shipments[id][field]


@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="Scalar API ")
