from http import HTTPStatus

from common.database_connection import get_db
from common.keycloak_connection import KeycloakConnection
from controller.course.CourseController import CourseController
from fastapi import APIRouter, Depends, Request

router = APIRouter(prefix="/api/v1/courses", tags=["courses"])


@router.get("")
async def list_course(client=Depends(get_db)):
    controller = CourseController(client=client)
    return await controller.list_course()
