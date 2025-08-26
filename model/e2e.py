from pydantic import BaseModel

class E2E(BaseModel):
    is_checkout_available: bool = None