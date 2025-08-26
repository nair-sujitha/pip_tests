from pydantic import BaseModel

class AddToCartChecks(BaseModel):
    is_add_to_cart_on_the_right: bool = None
    is_add_to_cart_below_delivery_details: bool = None
    is_add_to_cart_color_orange: bool = None