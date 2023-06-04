from typing import Optional
from pydantic import BaseModel

class ResponseModel(BaseModel):
    data: Optional[object]
    message: Optional[str]

class ListResponseModel(ResponseModel):
    total: Optional[int]