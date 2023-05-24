import os
from http import HTTPStatus

from common.helper import validate_token
from common.keycloak_connection import KeycloakConnection
from fastapi import APIRouter, Depends, Request

router = APIRouter()

@router.get("/login")
def login():
    authorization_url = KeycloakConnection().auth_url(
        redirect_uri="http://localhost:8000/callback",
        scope="openid profile",
    )
    return {"authorization_url": authorization_url}


@router.get("/callback")
def callback(request: Request, code: str):
    token = KeycloakConnection().token(
        code=code,
        redirect_uri=request.url_for("callback"),
        grant_type="authorization_code",
    )

    return {
        "success": True,
        "token": token,
    }, HTTPStatus.OK


@router.get("/check", dependencies=[Depends(validate_token)])
def check():
    return HTTPStatus.OK
