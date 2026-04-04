from random import randint
from pydantic import BaseModel,Field
from app.database.models import ShipmentStatus

def random_zip_code():
    return randint(11000, 11999)


class BaseShipment(BaseModel):
    content: str = Field(max_length=50, description="Description of the shipment content")
    weight: float = Field(gt=0, le=25, description="Weight must be a positive number and not exceed 25 kg")
    destination: str = Field(max_length=100, description="Destination of the shipment")
    zip_code: int | None = Field(default_factory=random_zip_code, description="it will be generated randomly if not provided")

class ShipmentRead(BaseShipment):
    shipment_status: ShipmentStatus = Field(description="Status of the shipment")

class ShipmentCreate(BaseShipment):
    pass

class ShipmentUpdate(BaseModel):
    content: str | None = Field(default=None, max_length=50)
    weight: float | None = Field(default=None, gt=0, le=25)
    destination: str | None  = Field(default=None, max_length=100)
    zip_code: int | None = Field(default= None)
    shipment_status: ShipmentStatus | None = Field(default=None)
