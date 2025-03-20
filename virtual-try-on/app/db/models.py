from sqlalchemy import Column, Integer, String
from app.db.base import Base

class TryOnImage(Base):
    __tablename__ = "tryon_images"

    id = Column(Integer, primary_key=True, index=True)
    human_image_url = Column(String, nullable=False)
    garment_image_url = Column(String, nullable=False)
    output_image_url = Column(String, nullable=False)  # Cloudinary URL
