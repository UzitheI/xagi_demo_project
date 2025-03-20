from fastapi import FastAPI
from app.api.endpoints import tryon, models, garments

app = FastAPI()

# Include API routes
app.include_router(tryon.router, prefix="/tryon", tags=["Try-On"])
app.include_router(models.router, prefix="/models", tags=["Models"])
app.include_router(garments.router, prefix="/garments", tags=["Garments"])

@app.get("/")
def root():
    return {"message": "Virtual Try-On API is running"}
