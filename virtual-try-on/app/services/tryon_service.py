import requests
import os
from app.core.config import settings
FAL_API_KEY = settings.FAL_KEY

def generate_tryon(human_image, garment_image):
    url = settings.FAL_URL
    headers = {"Authorization": f"Key {FAL_API_KEY}", "Content-Type": "application/json"}
    
    payload = {"human_image_url": human_image, "garment_image_url": garment_image}
    response = requests.post(url, json=payload, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("Failed to generate image")
