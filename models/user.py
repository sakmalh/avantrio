from pydantic import BaseModel, EmailStr, conlist, Field
from datetime import datetime
from models.item import ItemModel


class UserModel(BaseModel):
    user_id: str = Field(min_length=1)
    timestamp: datetime
    email: EmailStr
    items: conlist(item_type=ItemModel)
