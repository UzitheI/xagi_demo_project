import requests
import os
from dotenv import load_dotenv
import time

load_dotenv()  # Load .env variables
FAL_API_KEY = os.getenv("FAL_API_KEY")



FAL_URL = os.getenv("FAL_URL")

def generate_tryon(human_image: str, garment_image: str, poll_interval: int = 5, max_retries: int = 100):
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
        # Initial request
        response = requests.post(FAL_URL, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        
        status_url = data["status_url"]
        response_url = data["response_url"]

        # Polling the status
        for _ in range(max_retries):
            status_response = requests.get(status_url, headers=headers)
            status_response.raise_for_status()
            status_data = status_response.json()
            
            if status_data.get("status") == "COMPLETED":
                # Retrieve the generated image
                final_response = requests.get(response_url, headers=headers)
                final_response.raise_for_status()
                return final_response.json()  # This contains the image URL or data
            
            time.sleep(poll_interval)

        return {"error": "Timeout reached, image not generated."}

    except requests.exceptions.RequestException as e:
        return {"error": "Request failed", "details": str(e)}

