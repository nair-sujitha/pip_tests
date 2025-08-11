from pydantic import BaseModel

class Delivery(BaseModel):
    is_delivery_available: bool = None
    is_pickup_nearby_available: bool = None
    is_delivery_free: bool = None