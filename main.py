from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from api.routers.user_router import router as user_router


app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(user_router)


@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "home.html", {"request": request, "journalblog": "website"}
    )


# if __name__ == "__main__":
#     uvicorn.run(app)
