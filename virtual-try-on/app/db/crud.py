from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.base import Base
from app.db.models import HumanModel, Garment, OutputImage  # Your models here
from pydantic import BaseModel

router = APIRouter()

# --- Pydantic Schemas (Request/Response models) ---

class TryOnImageCreate(BaseModel):
    human_image_url: str
    garment_image_url: str
    output_image_url: str

class HumanModelCreate(BaseModel):
    name: str
    image_url: str

class GarmentCreate(BaseModel):
    name: str
    image_url: str

class OutputImageCreate(BaseModel):
    human_model_id: int
    garment_id: int
    output_image_url: str

@router.post("/human_models/", response_model=HumanModelCreate)
def create_human_model(human_model: HumanModelCreate, db: Session = Depends(get_db)):
    db_human_model = HumanModel(**human_model.dict())
    db.add(db_human_model)
    db.commit()
    db.refresh(db_human_model)
    return db_human_model

# --- API Routes for Garment ---

@router.post("/garments/", response_model=GarmentCreate)
def create_garment(garment: GarmentCreate, db: Session = Depends(get_db)):
    db_garment = Garment(**garment.dict())
    db.add(db_garment)
    db.commit()
    db.refresh(db_garment)
    return db_garment

# --- API Routes for OutputImage ---

@router.post("/output_images/", response_model=OutputImageCreate)
def create_output_image(output_image: OutputImageCreate, db: Session = Depends(get_db)):
    db_output_image = OutputImage(**output_image.dict())
    db.add(db_output_image)
    db.commit()
    db.refresh(db_output_image)
    return db_output_image