from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/", summary="Главная ручка", tags=["Основные ручки"])
def home():
    return "Hello"


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
