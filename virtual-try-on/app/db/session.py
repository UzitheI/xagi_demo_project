from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create declarative base
Base = declarative_base()

# Database connection settings
DB_USER = os.getenv("DB_USER")  
DB_PASSWORD = os.getenv("DB_PASSWORD")  
DB_HOST = os.getenv("DB_HOST")  
DB_PORT = os.getenv("DB_PORT")  
DB_NAME = os.getenv("DB_NAME")  

# PostgreSQL async database URL
SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create an async engine
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=1800
)

# Async session
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# Dependency to get a database session
async def get_db():
    async with SessionLocal() as session:
        yield session