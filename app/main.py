from typing import Any
from fastapi import FastAPI, HTTPException , status
from scalar_fastapi import get_scalar_api_reference
app = FastAPI()

shipments  = {
    12078: {
        "content" : "table",
        "weight" : .78,
        "destination" : "Paris"
    },
    12079: {
        "content" : "chair",
        "weight" : 0.5,
        "destination" : "London"
    },
    12080: {
        "content" : "bookshelf",
        "weight" : 2.3,
        "destination" : "Berlin"
    },
    12081: {
        "content" : "lamp",
        "weight" : 0.8,
        "destination" : "Rome"
    },
    12082: {
        "content" : "desk",
        "weight" : 1.5,
        "destination" : "Madrid"
    },
    12083: {
        "content" : "cabinet",
        "weight" : 3.2,
        "destination" : "Amsterdam"
    },
    12084: {
        "content" : "sofa",
        "weight" : 4.1,
        "destination" : "Vienna"
    }
}

@app.get("/shipment/latest")
def get_shipment_latest():
    return shipments[max(shipments.keys())]


@app.get("/shipment")
def get_shipment(id : int | None = None) -> dict[str, Any]:

    if id is None:
        return shipments[max(shipments.keys())]
    if id not in shipments:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                           detail="Givern ID not found")
    return shipments[id]

@app.post("/shipment")
def create_shipment(weight : float, destination : str, data : dict[str, Any]) -> dict[str, Any]:
    new_id = max(shipments.keys()) + 1
    content = data["content"]

    if weight <= 0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="Weight must be a positive number")
    
    if weight > 100:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, 
                            detail="Weight must not exceed 100 kg")
    shipments[new_id] = {
        "content" : content,
        "weight" : weight,
        "destination" : destination
    }
    return {
        "id" : new_id,
    }

@app.get("/shipments/{field}")
def get_shipments_fields(field : str, id : int) -> dict[str, Any]:
    return {
        field : shipments[id][field]
    }

@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API "
    )