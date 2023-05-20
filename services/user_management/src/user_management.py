from fastapi import FastAPI, Request
from keycloak import KeycloakOpenID

app = FastAPI()
keycloak_openid = KeycloakOpenID(server_url="http://localhost:8002/auth/realms",
                                client_id="LMS",
                                realm_name="LMS",
                                client_secret_key="8l7jCo37kNBCl9pMrNXkYkhQTWGm2TEf"
                                )

@app.get("/login")
def login(request: Request):
    # Obtain the authorization URL and redirect the user to Keycloak for login
    authorization_url = keycloak_openid.auth_url(
        redirect_uri="http://localhost:8000/callback",
        scope="openid profile",
    )
    return {"authorization_url": authorization_url}

@app.get("/callback")
def callback(request: Request, code: str):
    # Exchange the authorization code for tokens
    token = keycloak_openid.token(code=code, redirect_uri=request.url_for("callback"), grant_type="authorization_code")
    
    # Process the tokens and authenticate the user
    # Store the tokens or user information as required
    
    return {
        "success": True,
        "token": token,
    }

@app.get("/protected")
def protected(request: Request):
    # Example of a protected route that requires authentication
    token = keycloak_openid.get_token(request)
    
    # Validate the token and authorize access
    # Access user information if needed
    
    return {"message": "Access granted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("user_management:app", host="0.0.0.0", port=8000, reload="True")