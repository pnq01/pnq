from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def get_root():
    return {"data": "This is journal blog website for ksuae"}
