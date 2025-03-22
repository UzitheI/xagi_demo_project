from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.db.base import Base
from app.db.models import HumanModel, Garment, OutputImage
from pydantic import BaseModel

router = APIRouter()

# Pydantic model for creating a new Garment
class GarmentCreate(BaseModel):
    name: str
    image_url: str
    
    class Config:
        from_attributes = True  # Needed to work with ORM models

# Pydantic model for returning a Garment with ID
class GarmentResponse(BaseModel):
    id: int
    name: str
    image_url: str
    
    class Config:
        from_attributes = True

@router.post("/garments/", response_model=GarmentResponse)
async def create_garment(garment: GarmentCreate, db: AsyncSession = Depends(get_db)):
    # Create the Garment instance based on the Pydantic model
    db_garment = Garment(**garment.model_dump())  # Use dict() for Pydantic v1.x
    
    # Add to the database session
    db.add(db_garment)
    await db.commit()  # Commit the changes to the database
    await db.refresh(db_garment)  # Refresh the instance with the updated data from the database
    
    return db_garment  # Return the Garment object