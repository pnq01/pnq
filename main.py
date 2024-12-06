from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import uvicorn
from pydantic import BaseModel


app = FastAPI()

books = [
    {"id": 1, "title": "GRokaem algo", "author": "Ne pomnu"},
    {"id": 2, "title": "Linux and base", "author": "Danil Pa"},
]


@app.get("/", summary="начальная страница", tags=["Главная"])
def root():
    return FileResponse('index.html')


@app.get("/books", summary="Получение книжек", tags=["Книги"])
def read_books():
    return books


@app.get("/books/{book_id}", summary="Получение конкретной книжки", tags=["Книги"])
def get_one_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")


class NewBook(BaseModel):
    title: str
    author: str


@app.post("/books", summary="Добавление книжки", tags=["Книги"])
def add_book(new_book: NewBook):
    books.append(
        {
            "id": len(books) + 1,
            "title": new_book.title,
            "author": new_book.author,
        }
    )
    return {"success": True}


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
