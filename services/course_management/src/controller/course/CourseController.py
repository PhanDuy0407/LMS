from bson.objectid import ObjectId
from controller.model.Course import Course
from controller.model.ResponseModel import ListResponseModel, ResponseModel
from fastapi.responses import JSONResponse
from pymongo.collection import Collection


class CourseController:
    def __init__(self, client) -> None:
        self.client = client

    async def list_course(self) -> list:
        results = []
        collection: Collection = self.client["course"]
        courses = collection.find()
        async for course in courses:
            results.append(Course(**course))
        return JSONResponse(
            content=ListResponseModel(
                message="Success", data=results, total=len(results)
            ).dict(),
            status_code=200,
        )

    async def get_course(self, course_id) -> Course:
        collection: Collection = self.client["course"]
        course = await collection.find_one({"_id": ObjectId(course_id)})
        if not course:
            return JSONResponse(
                content=ResponseModel(message="Not Found").dict(), status_code=404
            )
        return JSONResponse(
            content=ResponseModel(message="Success", data=Course(**course)).dict(),
            status_code=200,
        )

    async def create_course(self, course_id) -> Course:
        collection: Collection = self.client["course"]
        course = await collection.find_one({"_id": ObjectId(course_id)})
        if not course:
            return JSONResponse(content={"data": "Not Found"}, status_code=404)
        course = dict(course)
        course["id"] = str(course["_id"])
        return JSONResponse(content={"data": Course(**course).dict()}, status_code=200)
