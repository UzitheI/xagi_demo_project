import cloudinary
import cloudinary.uploader
import os
from app.core.config import settings
cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_API_SECRET,
)

def upload_image(image_path):
    result = cloudinary.uploader.upload(image_path)
    return result["secure_url"]
