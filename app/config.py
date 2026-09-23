import os 
from dotenv import load_dotenv

load_dotenv()

class Settings:
    app_name=os.getenv("APP_NAME","Production AI API")
    environment = os.getenv("ENVIRONMENT","development")


settings=Settings()