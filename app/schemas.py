from pydantic import BaseModel


class Shipment(BaseModel):
    content: str
    weight: float
    destination: str
    shipment_status: str