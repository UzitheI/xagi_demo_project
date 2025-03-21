from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import tryon, models, garments

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include API routes
app.include_router(tryon.router, prefix="/tryon", tags=["Try-On"])
app.include_router(models.router, prefix="/models", tags=["Model"])
app.include_router(garments.router, prefix="/garments", tags=["Garment"])

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message": "Welcome to Virtual Try-On API", "status": "online"}

# Optional: Add a specific route for index.html if needed
@app.get("/index.html")
async def serve_index():
    from fastapi.responses import FileResponse
    return FileResponse("static/index.html")