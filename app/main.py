from typing import Any
from fastapi import FastAPI
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
        return {"error": "Shipment not found"}
    return shipments[id]



@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API "
    )