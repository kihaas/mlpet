import uvicorn
from pydantic import BaseModel, Field, ConfigDict
from fastapi import FastAPI, HTTPException

app = FastAPI()
#
# @app.get("/", summary="ееее", tags=["книжонки"])
# def root():
#     return {"message": "Hello World"}
#
# books = [
#     {
#         "id": 1,
#         "title": "Book 1",
#         "author": "Author 1"
#     },
#     {
#         "id": 2,
#         "title": "Book 2",
#         "author": "Author 2"
#     }
# ]
# @app.get("/books")
# def read_books():
#     return books
#
# @app.get("/books/{book_id}")
# def get_book(book_id: int):
#     for book in books:
#         if book["id"] == book_id:
#             return book
#     raise HTTPException(status_code=404, detail="Book not found")
#
# class NewBook(BaseModel):
#     title: str
#     author: str

#padentic
data = {
    "email": "abc@mail.com",
    "bio": "<3",
    "age": 12
}

data_wo_age = {
    "email": "abc@mail.com",
    "bio": "<3",
    # "gender": "male",
    # "birthday": "2022"
}





class UserSchema(BaseModel):
    email: str
    bio: str | None = Field(max_length=10)

    model_config = ConfigDict(extra ='forbid')

class UserAgeSchema(UserSchema):
    age: int | None = Field(default=None, ge=0, le=130)

# print(repr(UserAgeSchema(**data_wo_age)))
# print(repr(UserSchema(**data)))

users = []

@app.post("/users")
def add_user(user: UserSchema):
    users.append(user.model_dump())
    return {"ok": True, "msg": "user added"}

@app.get("/users")
def get_users():
    return users



# def func(data: dict):
#     data["age"] += 1
#
#
# @app.post("/books")
# def create_books(new_book: NewBook):
#     books.append({
#         "id": len(books) + 1,
#         "title": new_book.title,
#         "author": new_book.author,
#     })
#     return {"message": "Book created"}
#
#
#
# if __name__ == "__main__":
#     uvicorn.run("main:app",reload=True)