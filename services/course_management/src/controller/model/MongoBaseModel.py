from pydantic import BaseModel

class MongoBaseModel(BaseModel):
    def __init__(self, **data):
        if "_id" in data:
            data["id"] = str(data.pop("_id"))
        super().__init__(**data)