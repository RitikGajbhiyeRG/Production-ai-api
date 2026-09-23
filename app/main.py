from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return {"MEssage : production app is running !!!"}