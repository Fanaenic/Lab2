from fastapi import FastAPI
from wikipedia import *
from pydantic import BaseModel

app= FastAPI()

class wiki_search(BaseModel):
    name: str

@app.get("/wikipedia/{name}")
def path(name: str):
    return {"result" : wikipedia.page(name).content}

@app.get("/wikipedia/query")
def query(name: str):
    return {"result" : wikipedia.page(name).content}

@app.post("/wikipedia/search_body")
def post_body(name: str):
    return {"result" : wikipedia.page(name).content}

