from fastapi import FastAPI
from app.config import settings
from app.error import general_exception_handler


from app.logger import logger
app = FastAPI(title=settings.app_name)
logger.info("Application started")


# Tell FastAPI:
# If an unexpected Python error happens,
# use our custom error handler.
app.add_exception_handler(
    Exception,
    general_exception_handler
)


@app.get("/")
def home():
    logger.info("Home endpoint was called")
    return {
        "message": "Production AI API is running",
        "environment": settings.environment
    }


@app.get("/test-error")
def error():
    return{
        "message":"nikal ja lawde"
    }