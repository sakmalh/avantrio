from pydantic import BaseModel, Field


class ItemModel(BaseModel):
    item_id: str = Field(min_length=1)
    quantity: int = Field(gt=0)
    price: float = Field(gt=0)

