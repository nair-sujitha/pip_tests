from pydantic import BaseModel

class ProductProps(BaseModel):
    price: str
    is_protection_plan_available: bool
    is_delivery_free: bool