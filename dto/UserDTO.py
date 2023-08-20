from pydantic import BaseModel, Field
from typing import Optional
class UserDTO(BaseModel):
    id: Optional[int] 
    username : str
    description: str | None = Field(
        default=None, title="The description of the item", max_length=300
    )

    