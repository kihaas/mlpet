import uvicorn

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/", summary="ееее", tags=["base"])
def root():
    return {"message": "Hello World"}

books = [
    {
        "id": 1,
        "title": "Book 1",
        "author": "Author 1"
    },
    {
        "id": 2,
        "title": "Book 2",
        "author": "Author 2"
    }
]
@app.get("/books")
def read_books():
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


if __name__ == "__main__":
    uvicorn.run("main:app",reload=True)