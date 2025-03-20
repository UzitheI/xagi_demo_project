import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME", "Virtual-Try-On")
    DEBUG = os.getenv("DEBUG", "True").lower() == "true"
    HOST = os.getenv("HOST", "127.0.0.1")
    PORT = int(os.getenv("PORT", 8000))

    # Database settings
    DB_USER = os.getenv("DB_USER")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_HOST = os.getenv("DB_HOST")
    DB_PORT = os.getenv("DB_PORT")
    DB_NAME = os.getenv("DB_NAME")

    # Kolors API
    FAL_KEY = os.getenv("FAL_KEY")
    FAL_URL = os.getenv("FAL_URL")

    # Cloudinary
    CLOUDINARY_CLOUD_NAME = os.getenv("CLOUDINARY_CLOUD_NAME")
    CLOUDINARY_API_KEY = os.getenv("CLOUDINARY_API_KEY")
    CLOUDINARY_API_SECRET = os.getenv("CLOUDINARY_API_SECRET")

    # Secret key (for authentication, if needed)
    SECRET_KEY = os.getenv("SECRET_KEY")

settings = Settings()
