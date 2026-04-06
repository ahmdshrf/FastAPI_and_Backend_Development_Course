from contextlib import asynccontextmanager
from datetime import datetime, timedelta
from typing import Any

from fastapi import  FastAPI, HTTPException, status
from scalar_fastapi import get_scalar_api_reference

from app.database.models import ShipmentStatus
from app.database.session import SessionDep, create_db_tables

from .schemas import (  #you can also import Shipment from app.schemas if you want to run the code outside of the app directory
    ShipmentCreate,
    Shipment,
    ShipmentUpdate,
)


@asynccontextmanager
async def lifespan_handler(app : FastAPI):
    create_db_tables()
    yield

app = FastAPI(lifespan=lifespan_handler)

# db = Database()
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


# @app.get("/shipment/latest", response_model=Shipment)
# def get_shipment_latest() -> dict[str, Any] | None:
#     latest_shipment = db.get_latest_shipment()
#     if latest_shipment is None:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="Givern ID not found"
#         )
#     return latest_shipment

@app.get("/shipment", response_model=Shipment)
def get_shipment(id: int, session : SessionDep ) -> Shipment :
    shipment = session.get(Shipment,id)
    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Givern ID not found"
        )
    return shipment




@app.post("/shipment")
def create_shipment(
    shipment: ShipmentCreate,
    session : SessionDep
) -> dict[str, int]:
    new_shipment = Shipment(
        **shipment.model_dump(),
        shipment_status=ShipmentStatus.PLACED,
        estimated_delivery=datetime.now() + timedelta(days=3)
    )
    session.add(new_shipment)
    session.commit()
    session.refresh(new_shipment)
    return {"id": new_shipment.id}


@app.patch("/shipment", response_model=Shipment)
def update_shipment(
    id: int,
    shipment_update: ShipmentUpdate,
    session: SessionDep
):
    update = shipment_update.model_dump(exclude_none=True)
    if update is None :
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="No Data provided"
        )
    shipment = session.get(Shipment, id)
    if shipment is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Given ID not found"
        )
    shipment.sqlmodel_update(update)
    session.add(shipment)
    session.commit()
    session.refresh(shipment)
    return shipment

@app.delete("/shipment")
def delete_shipment(id: int,session : SessionDep) -> dict[str, Any]:
    session.delete(
        session.get(Shipment,id)
    )
    session.commit()
    return {"detail": f"Shipment with ID {id} has been deleted"}

# @app.get("/shipments/{field}")
# def get_shipments_fields(field: str, id: int) -> Any:
#     return shipments[id][field]


@app.get("/scalar", include_in_schema=False)
def get_scalar_docs():
    return get_scalar_api_reference(openapi_url=app.openapi_url, title="Scalar API ")
