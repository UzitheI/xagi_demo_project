from fastapi import FastAPI, Depends, HTTPException, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.db.models import HumanModel, Garment, OutputImage
from pydantic import BaseModel
from typing import List

# Pydantic model for OutputImage
class OutputImageBase(BaseModel):
    id: int
    human_model_id: int
    garment_id: int
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

# OutputImageCreate response model
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
async def create_human_model(human_model: HumanModelCreate, db: AsyncSession = Depends(get_db)):
    db_human_model = HumanModel(**human_model.model_dump())  # Use model_dump() for Pydantic v2 or dict() for v1
    db.add(db_human_model)
    await db.commit()
    await db.refresh(db_human_model)
    return db_human_model

# Create OutputImage
@router.post("/output_images/", response_model=OutputImageResponse)
async def create_output_image(output_image: OutputImageCreate, db: AsyncSession = Depends(get_db)):
    db_output_image = OutputImage(**output_image.model_dump())  # Use model_dump() for Pydantic v2 or dict() for v1
    db.add(db_output_image)
    await db.commit()
    await db.refresh(db_output_image)
    return db_output_image

@router.put("/output_images/{output_image_id}", response_model=OutputImageResponse)
async def update_output_image(output_image_id: int, output_image_update: OutputImageCreate, db: AsyncSession = Depends(get_db)):
    # Retrieve the existing OutputImage record from the database
    db_output_image = await db.get(OutputImage, output_image_id)
    
    if not db_output_image:
        raise HTTPException(status_code=404, detail="OutputImage not found")
    
    # Update the fields of the OutputImage record
    db_output_image.output_image_url = output_image_update.output_image_url
    
    # Save the changes to the database
    await db.commit()
    
    return db_output_image


# Get OutputImages by HumanModel ID
@router.get("/output_images/human/{human_model_id}", response_model=List[OutputImageBase])
async def get_output_images_by_human(human_model_id: int, db: AsyncSession = Depends(get_db)):
    # Use select() from SQLAlchemy to get output images filtered by human_model_id
    result = await db.execute(
        select(OutputImage).where(OutputImage.human_model_id == human_model_id)
    )
    output_images = result.scalars().all()
    return output_images

# Get OutputImages by Garment ID
@router.get("/output_images/garment/{garment_id}", response_model=List[OutputImageBase])
async def get_output_images_by_garment(garment_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        OutputImage.__table__.select().where(OutputImage.garment_id == garment_id)
    )
    output_images = result.scalars().all()
    return output_images

from sqlalchemy import select
from typing import List
@router.get("/models", response_model=List[HumanModelBase])
async def get_all_human_models(db: AsyncSession = Depends(get_db)):
    # Use select() from SQLAlchemy to get all models
    result = await db.execute(select(HumanModel))
    # Get all results as model objects
    human_models = result.scalars().all()
    return human_models

@router.get("/garments", response_model=List[GarmentBase])
async def get_all_garments(db: AsyncSession = Depends(get_db)):
    # Use select() from SQLAlchemy to get all garments
    result = await db.execute(select(Garment))
    # Get all results as model objects
    garments = result.scalars().all()
    return garments