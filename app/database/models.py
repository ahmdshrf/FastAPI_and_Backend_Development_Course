from enum import Enum
from sqlmodel import Field, SQLModel


class ShipmentStatus(str, Enum):
    PENDING = "pending"
    IN_TRANSIT = "in_transit"
    DELIVERED = "delivered"
    PLACED = "placed"
    OUT_FOR_DELIVERY = "out_for_delivery"

class Shipment(SQLModel) :
    __tablename__ = "shipment"
    id : int
    content : str
    weight : float
    destination : int
    shipment_status : ShipmentStatus = Field(description="Status of the shipment")
    estimated_delivery : str