from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.tryon_service import generate_tryon
router = APIRouter()

class TryOnRequest(BaseModel):
    human_image_url: str
    garment_image_url: str

from fastapi import HTTPException

@router.post("/generate")
def generate_tryon_image(request: TryOnRequest):
    try:
        # Call the generate_tryon function with the URLs from the request
        result = generate_tryon(
            human_image=request.human_image_url,
            garment_image=request.garment_image_url
        )
        return result
    except Exception as e:
        # Proper FastAPI error handling
        raise HTTPException(status_code=500, detail=f"Failed to generate image: {str(e)}")
