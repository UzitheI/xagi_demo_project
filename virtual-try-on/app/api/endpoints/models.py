from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.db.models import HumanModel, Garment, OutputImage  # Your models here
from pydantic import BaseModel
from typing import List

# Pydantic model for OutputImage
class OutputImageBase(BaseModel):
    id: int
    human_model_id:int
    garment_id:int
    output_image_url: str

    class Config:
        from_attributes = True  # Allow SQLAlchemy objects to be converted to Pydantic models

# Pydantic model for HumanModel
class HumanModelBase(BaseModel):
    id: int
    name: str
    image_url: str

    class Config:
        from_attributes = True

# Pydantic model for Garment
class GarmentBase(BaseModel):
    id: int
    name: str
    image_url: str

    class Config:
        from_attributes = True

# Pydantic model for creating a HumanModel
class HumanModelCreate(BaseModel):
    name: str
    image_url: str

# Pydantic model for creating an OutputImage
class OutputImageCreate(BaseModel):
    human_model_id: int
    garment_id: int
    output_image_url: str

# OutputImageCreate response model (can be the same as OutputImageBase)
class OutputImageResponse(BaseModel):
    id: int
    human_model_id: int
    garment_id: int
    output_image_url: str

    class Config:
        from_attributes = True

router = APIRouter()

# Create HumanModel
@router.post("/human_models/", response_model=HumanModelBase)
def create_human_model(human_model: HumanModelCreate, db: Session = Depends(get_db)):
    db_human_model = HumanModel(**human_model.dict())  # Use dict() for Pydantic v1
    db.add(db_human_model)
    db.commit()
    db.refresh(db_human_model)
    return db_human_model

# Create OutputImage
@router.post("/output_images/", response_model=OutputImageResponse)
def create_output_image(output_image: OutputImageCreate, db: Session = Depends(get_db)):
    db_output_image = OutputImage(**output_image.dict())  # Use dict() for Pydantic v1
    db.add(db_output_image)
    db.commit()
    db.refresh(db_output_image)
    return db_output_image

# Get OutputImages by HumanModel ID
@router.get("/output_images/human/{human_model_id}", response_model=List[OutputImageBase])
def get_output_images_by_human(human_model_id: int, db: Session = Depends(get_db)):
    output_images = db.query(OutputImage).filter(OutputImage.human_model_id == human_model_id).all()
    return output_images

# Get OutputImages by Garment ID
@router.get("/output_images/garment/{garment_id}", response_model=List[OutputImageBase])
def get_output_images_by_garment(garment_id: int, db: Session = Depends(get_db)):
    output_images = db.query(OutputImage).filter(OutputImage.garment_id == garment_id).all()
    return output_images

@router.get("/models", response_model=List[HumanModelBase])
def get_output_images_by_garment(db: Session = Depends(get_db)):
    output_images = db.query(HumanModel).all()
    return output_images

@router.get("/garments", response_model=List[GarmentBase])
def get_output_images_by_garment(db: Session = Depends(get_db)):
    output_images = db.query(Garment).all()
    return output_images


