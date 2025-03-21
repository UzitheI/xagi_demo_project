from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.tryon_service import generate_tryon
from fastapi.responses import JSONResponse,RedirectResponse
router = APIRouter()

class TryOnRequest(BaseModel):
    human_image_url: str
    garment_image_url: str

import requests
from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import StreamingResponse
from io import BytesIO
from dotenv import load_dotenv
load_dotenv()
import os
FAL_API_KEY= os.getenv("FAL_API_KEY")


@router.get("/view_image/")
async def view_image(response_url: str):
    try:
        # Make the request to the URL with the authentication header
        headers = {"Authorization": f"Key {FAL_API_KEY}"}
        response = requests.get(response_url, headers=headers)
        
        # If the request was successful, return the image
        if response.status_code == 200:
            return StreamingResponse(BytesIO(response.content), media_type="image/jpeg")
        else:
            raise HTTPException(
                status_code=response.status_code, 
                detail=f"Failed to fetch the image. Status code: {response.status_code}, Response: {response.text}"
            )
    
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 401:
            raise HTTPException(status_code=401, detail="Authentication required to access this URL")
        raise HTTPException(status_code=500, detail=f"HTTP Error: {str(e)}")
    
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Request Error: {str(e)}")
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Unexpected error: {str(e)}")

    
   
@router.post("/generate_tryon")
async def generate_tryon_endpoint(human_image: str, garment_image: str):
    print("The api key is ", FAL_API_KEY)
    result = generate_tryon(human_image, garment_image)

    print("The result is ", result)

    if isinstance(result, dict) and "error" in result:
        return JSONResponse(content=result, status_code=400)

    if isinstance(result, dict) and "error" in result:
        return JSONResponse(content=result, status_code=400)

    # If result is a dictionary with the "response_url" key, return it as a response
    elif isinstance(result, dict) and "response_url" in result:
        return JSONResponse(content=result, status_code=200)

    # If result is image data, return it as a response
    elif isinstance(result, bytes):
        return Response(content=result, media_type="image/jpeg")

    else:
        # Log the error message
        print(f"Invalid response from FAL API: {result}")

        # Return a custom error response
        return JSONResponse(content={"error": "Invalid response from FAL API"}, status_code=500)