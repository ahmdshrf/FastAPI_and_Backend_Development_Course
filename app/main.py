from typing import Any
from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference
app = FastAPI()

@app.get("/shipment/latest")
def get_shipment_latest():
    return {
            "id" : 123456,
            "content" : "table",
            "weight" : .78,
            "destination" : "Paris"
            }


@app.get("/shipment/{id}")
def get_shipment(id : int) -> dict[str, Any]:
    return {
            "id" : id,
            "content" : "wooden table",
            "weight" : 10.78,
            "destination" : "New York"
            }



@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title="Scalar API "
    )