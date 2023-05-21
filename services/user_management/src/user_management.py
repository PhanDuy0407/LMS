import os

from dotenv import load_dotenv
from fastapi import FastAPI, Request
from keycloak import KeycloakOpenID

app = FastAPI()
keycloak_openid = KeycloakOpenID(
    server_url=os.getenv("SERVER_URL"),
    client_id=os.getenv("CLIENT_ID"),
    realm_name=os.getenv("REALM_NAME"),
    client_secret_key=os.getenv("CLIENT_SECRET"),
)


@app.get("/login")
def login():
    authorization_url = keycloak_openid.auth_url(
        redirect_uri="http://localhost:8000/callback",
        scope="openid profile",
    )
    return {"authorization_url": authorization_url}


@app.get("/callback")
def callback(request: Request, code: str):
    token = keycloak_openid.token(
        code=code,
        redirect_uri=request.url_for("callback"),
        grant_type="authorization_code",
    )

    return {
        "success": True,
        "token": token,
    }


if __name__ == "__main__":
    import uvicorn

    load_dotenv()
    uvicorn.run("user_management:app", host="0.0.0.0", port=8000, reload="True")
