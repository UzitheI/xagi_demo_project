import requests
import os
from app.core.config import settings
FAL_API_KEY = settings.FAL_KEY

from dotenv import load_dotenv
import os

load_dotenv()  # Load .env variables
FAL_API_KEY = os.getenv("FAL_API_KEY")

FAL_URL = os.getenv("FAL_URL", "https://queue.fal.run/fal-ai/kling/v1-5/kolors-virtual-try-on")

def generate_tryon(human_image: str, garment_image: str):
    if not FAL_API_KEY:
        return {"error": "API key is missing. Set FAL_API_KEY in environment variables."}

    headers = {
        "Authorization": f"Key {FAL_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "human_image_url": human_image,
        "garment_image_url": garment_image,
    }

    try:
        response = requests.post(FAL_URL, json=payload, headers=headers)
        response.raise_for_status()

        # Return the entire JSON response
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": "HTTP error", "details": response.text if response else str(e)}
    except requests.exceptions.RequestException as e:
        return {"error": "Request failed", "details": str(e)}
