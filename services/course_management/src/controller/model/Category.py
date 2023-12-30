from typing import Optional

from pydantic import BaseModel


class Category(BaseModel):
    id: str
    name: str
    description: Optional[str]
