from fastapi import FastAPI, Body
import os

stage = os.environ.get("DEV","PRD")

app = FastAPI()

#----
BOOKS = [{"Title":"Vidas secas", "Author":"Graciliano Ramos"}, {"Title":"Crime e castigo","Author":"Dostoievsk"}, 
            {"Title":"Noites brancas","Author":"Dostoievsk"}]

@app.get("/")
def index():
    return {"Hell": "World"}

# Static Path
@app.get("/books")
async def books():
    return BOOKS

# Path parameters
@app.get("/books/{number}")
async def books(number):
    try:
        return BOOKS[int(number)]
    except:
        return "Not FOund"



# Query parameters on request = author/?Author=<something> !! 
@app.get("/author/{author}")
async def spec_auth_by_query(author:str):
    spec_book = []
    try:
        for book in BOOKS:
            if book["Author"] == author:
                spec_book.append(book)

        return spec_book
    except Exception as err:
        print(err)
        return "Not Found"

@app.post("/books/create_book")
async def create_books(new_book = Body()):
    BOOKS.append(new_book)
    print(BOOKS)

#update 
@app.py("/books/update_book")
async def update_book(update_book = Body()):
    for i in range(len(BOOKS)):
        if BOOKS[i].get('title').casefold() == update_book.get('title').casefold():
            BOOKS[i] = update_book