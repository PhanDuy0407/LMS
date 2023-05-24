from api.auth import router as auth
from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI()
app.include_router(auth)

if __name__ == "__main__":
    import uvicorn

    load_dotenv()
    uvicorn.run("course_management:app", host="0.0.0.0", port=8000, reload="True")
