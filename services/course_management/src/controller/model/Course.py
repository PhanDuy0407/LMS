from typing import Optional
from controller.model.MongoBaseModel import MongoBaseModel
from controller.model.Category import Category

class Course(MongoBaseModel):
    id: str
    name: str
    description: Optional[str]
    category: Optional[Category]
    teacher: Optional[dict]
