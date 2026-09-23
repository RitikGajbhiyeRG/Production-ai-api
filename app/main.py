import dotenv
from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

app=FastAPI()


app_name=os.getenv("APP_NAME","Production AI API")

environment=os.getenv("ENVIRONMENT","development")


@app.get("/")
def home():
    return {"MEssage": "production app is running !!!",
    "environment": environment}