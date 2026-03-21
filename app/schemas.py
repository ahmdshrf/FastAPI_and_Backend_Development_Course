from pydantic import BaseModel,Field


class Shipment(BaseModel):
    content: str = Field(max_length=50, description="Description of the shipment content")
    weight: float = Field(gt=0, le=25, description="Weight must be a positive number and not exceed 25 kg")
    destination: str = Field(max_length=100, description="Destination of the shipment")
    shipment_status: str = Field(max_length=20, description="Status of the shipment")