# this is a simple FastAPI code written for demonstration, anyone can use this as a template and populate this file.

from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"Message": "Hello world!"}