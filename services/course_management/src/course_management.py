from dotenv import load_dotenv
from fastapi import FastAPI
from router import routers

app = FastAPI()
for router in routers:
    app.include_router(router)

if __name__ == "__main__":
    import uvicorn

    load_dotenv()
    uvicorn.run("course_management:app", host="0.0.0.0", port=8000, reload="True")
