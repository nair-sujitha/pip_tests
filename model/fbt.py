from pydantic import BaseModel

class FrequentlyBoughtTogether(BaseModel):
    number_of_items_listed: int = 0
    is_add_items_to_cart_button_enabled: bool = None
    add_items_to_cart_button_text: str = None