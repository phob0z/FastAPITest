from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/algo")
def root():
    return "Hola"