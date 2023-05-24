import os
import requests
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from common.keycloak_connection import KeycloakConnection

security = HTTPBearer()


def validate_token(auth: HTTPAuthorizationCredentials = Depends(security)):
    token = auth.credentials
    url = f"{os.getenv('SSO_URL')}/{os.getenv('REALM_NAME')}/protocol/openid-connect/userinfo"
    headers = {"Authorization": f"Bearer {token}"}
    check_user_response = requests.get(url=url, headers=headers)
    KEYCLOAK_PUBLIC_KEY = "-----BEGIN PUBLIC KEY-----\n" + KeycloakConnection().public_key() + "\n-----END PUBLIC KEY-----"
    options = {"verify_signature": True, "verify_aud": False, "verify_exp": False}
    decoded_token = KeycloakConnection().decode_token(token, key=KEYCLOAK_PUBLIC_KEY, options=options)
    print(decoded_token)
    if not check_user_response:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="UNAUTHORIZED",
        )
    return token
