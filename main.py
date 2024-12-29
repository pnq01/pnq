from fastapi import FastAPI, Depends

from .src.api.router import router as user_router


app = FastAPI()

app.include_router(user_router)

# if __name__ == "__main__":
#     uvicorn.run(app)
