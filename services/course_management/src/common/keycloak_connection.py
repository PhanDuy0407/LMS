import os

from keycloak import KeycloakOpenID


class KeycloakConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = KeycloakOpenID(
                server_url=os.getenv("SSO_URL"),
                client_id=os.getenv("CLIENT_ID"),
                realm_name=os.getenv("REALM_NAME"),
                client_secret_key=os.getenv("CLIENT_SECRET"),
            )

        return cls._instance
