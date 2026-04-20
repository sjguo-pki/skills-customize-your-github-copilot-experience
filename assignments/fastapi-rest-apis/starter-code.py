from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()


class BookInput(BaseModel):
    title: str
    author: str


# In-memory sample data (replace or extend as needed)
books = [
    {"id": 1, "title": "The Pragmatic Programmer", "author": "Andrew Hunt"},
    {"id": 2, "title": "Refactoring", "author": "Martin Fowler"},
]


@app.get("/books")
def get_books():
    return books


@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@app.post("/books")
def create_book(book_input: BookInput):
    new_id = max((book["id"] for book in books), default=0) + 1
    new_book = {
        "id": new_id,
        "title": book_input.title,
        "author": book_input.author,
    }
    books.append(new_book)
    return new_book


@app.put("/books/{book_id}")
def update_book(book_id: int, book_input: BookInput):
    for book in books:
        if book["id"] == book_id:
            book["title"] = book_input.title
            book["author"] = book_input.author
            return book
    raise HTTPException(status_code=404, detail="Book not found")
