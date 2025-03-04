import asyncio
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from src.api_v1.crud.demo_auto_crud import demo_m2m
from src.api_v1.routers import router as main_router
from src.core.config import static_files, templates
from src.db.database import (
    async_session_factory,
)

app = FastAPI(
    title="Journal Blog",
    contact={
        "name": "Danil",
        "url": "https://t.me/unsurpassed_talant",
        "email": "danpavkzn@mail.ru",
    },
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
)

app.mount("/static", static_files, name="static")
app.include_router(main_router)


# Переработать так как это SSR а нам нужно полностью по rest api
@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {
            "request": request,
        },
    )


async def main():
    # await drop_tables()
    # await create_tables()
    async with async_session_factory() as session:
        await demo_m2m(session)


if __name__ == "__main__":
    asyncio.run(main())
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
