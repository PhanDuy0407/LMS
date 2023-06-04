from controller.model.Course import Course
from fastapi.responses import JSONResponse


class CourseController:
    def __init__(self, client) -> None:
        self.client = client

    async def list_course(self) -> list:
        results = []
        collection = self.client["course"]
        courses = collection.find()
        async for course in courses:
            course = dict(course)
            course["id"] = str(course["_id"])
            results.append(Course(**course).dict())
        return JSONResponse(content={"data": results}, status_code=200)
    
    async def list_enroll(self, keys) -> list:
        results = []
        collection = self.client["course"]
        courses = collection.find()
        async for course in courses:
            course = dict(course)
            course["id"] = str(course["_id"])
            results.append(Course(**course).dict())
        return JSONResponse(content={"data": results}, status_code=200)
