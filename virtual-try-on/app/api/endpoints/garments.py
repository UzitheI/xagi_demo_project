from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.base import Base
from app.db.models import HumanModel, Garment, OutputImage  # Your models here
from pydantic import BaseModel

router = APIRouter()
# Pydantic model for creating a new Garment
class GarmentCreate(BaseModel):
    name: str
    image_url: str
    
    class Config:
        orm_mode = True  # Needed to work with ORM models
    
@router.post("/garments/", response_model=GarmentCreate)
def create_garment(garment: GarmentCreate, db: Session = Depends(get_db)):
    # Create the Garment instance based on the Pydantic model
    db_garment = Garment(**garment.model_dump())  # Use dict() for Pydantic v1.x
    
    # Add to the database session
    db.add(db_garment)
    db.commit()  # Commit the changes to the database
    db.refresh(db_garment)  # Refresh the instance with the updated data from the database

    return db_garment  # Return the Garment object