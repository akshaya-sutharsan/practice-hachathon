import os
from datetime import timedelta

from dotenv import load_dotenv

load_dotenv()

class Config:
    DB_USER =os.getenv("DB_USER")
    DB_PASSWORD =os.getenv("DB_PASSWORD")
    DB_HOST =os.getenv("DB_HOST")
    DB_NAME =os.getenv("DB_NAME")


    SQLALCHEMY_DATABASE_URI = (
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    )
    
    SQLALCHEMY_TRACK_MODEFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(
        minutes = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRES_MINUTES"))
    )

