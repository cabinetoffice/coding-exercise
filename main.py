"""Main module to run my simple API for my coding exercise"""

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 
    'This is a simple API for my coding exercise. Please visit /docs or /redoc for more information on how to use it.'}

@app.get('/hello')
async def hello():
    return {'message': 'Hello World!'}

@app.get("/add")
async def add(num1: int, num2: int):
    return {'result': num1 + num2}

@app.get("/addwords")
async def addwords(word1: str, word2: str):
    return {'result': f"{word1}-{word2}"}
