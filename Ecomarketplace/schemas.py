from pydantic import BaseModel
from typing import List, Optional

class ProductCreate(BaseModel):
    name: str
    description: str
    quantity: int
    price_per_unit: float
    is_verified: bool = False

class LocationCoordinates(BaseModel):
    latitude: float
    longitude: float

class RecyclingItemCreate(BaseModel):
    material_type: str
    quantity_available: float
    location: LocationCoordinates