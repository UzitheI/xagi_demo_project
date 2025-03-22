# This file re-exports all models to ensure they're registered with Base
from app.db.session import Base
from app.db.models import HumanModel, Garment, OutputImage