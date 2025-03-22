from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.session import Base  # Import Base from session.py, not create a new one

class HumanModel(Base):
    __tablename__ = "human_models"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    image_url = Column(String(255), nullable=False)

class Garment(Base):
    __tablename__ = "garments"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    image_url = Column(String(255), nullable=False)

class OutputImage(Base):
    __tablename__ = "output_images"
    
    id = Column(Integer, primary_key=True, index=True)
    human_model_id = Column(Integer, ForeignKey("human_models.id"))
    garment_id = Column(Integer, ForeignKey("garments.id"))
    output_image_url = Column(String(255), nullable=False)
    
    human_model = relationship("HumanModel", back_populates="output_images")
    garment = relationship("Garment", back_populates="output_images")

# Establish relationships
HumanModel.output_images = relationship("OutputImage", back_populates="human_model")
Garment.output_images = relationship("OutputImage", back_populates="garment")