from datetime import datetime
from random import randint
from pydantic import BaseModel
from sqlmodel import Field, SQLModel
from app.database.models import ShipmentStatus

def random_zip_code():
    return randint(11000, 11999)


class BaseShipment(SQLModel):
    content: str = Field(max_length=50, description="Description of the shipment content")
    weight: float = Field(gt=0, le=25, description="Weight must be a positive number and not exceed 25 kg")
    destination: str = Field(max_length=100, description="Destination of the shipment")
    zip_code: int | None = Field(default_factory=random_zip_code, description="it will be generated randomly if not provided")

class Shipment(BaseShipment,table = True):
    id : int = Field(default=None,primary_key=True)
    shipment_status: ShipmentStatus = Field(description="Status of the shipment")
    estimated_delivery: datetime


class ShipmentCreate(BaseShipment):
    pass

class ShipmentUpdate(BaseModel):
    shipment_status: ShipmentStatus | None = Field(default=None)
    estimated_delivery: datetime | None = Field(default=None)
    

