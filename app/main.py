from fastapi import FastAPI
from app.config import settings
from app.error import general_exception_handler

app = FastAPI(title=settings.app_name)

# Tell FastAPI:
# If an unexpected Python error happens,
# use our custom error handler.
app.add_exception_handler(
    Exception,
    general_exception_handler
)


@app.get("/")
def home():
    return {
        "message": "Production AI API is running",
        "environment": settings.environment
    }


