"""Main module to run my simple API for my coding exercise"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def root():
    return {
        "message": "This is a simple API for my coding exercise. "
        "Please visit /docs or /redoc for more information on how to use it."
    }


@app.get("/say-hello")
def hello():
    """Returns a hello world message in JSON"""
    return {"message": "Hello World!"}


@app.get("/add")
def add(num1: int, num2: int):
    """Takes two numbers and returns the result of the addition."""
    return {"result": num1 + num2}


@app.get("/join-words")
def addwords(word1: str, word2: str):
    """Takes two words and returns a joined word separated by a dash."""
    return {"result": f"{word1}-{word2}"}
