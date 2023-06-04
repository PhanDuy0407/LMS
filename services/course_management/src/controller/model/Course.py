from typing import Optional
from pydantic import BaseModel
from controller.model.Category import Category

class Course(BaseModel):
    id: str
    name: str
    description: Optional[str]
    category: Optional[Category]
    teacher: Optional[dict]
