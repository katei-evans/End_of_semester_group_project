from pydantic import BaseModel
from typing import List, Optional

# Producer & Inventory Schemas
class ProductCreate(BaseModel):
    name: str
    description: str
    quantity: int
    price_per_unit: float
    is_verified: bool = False

# Location Schema for Geo-Matching
class LocationCoordinates(BaseModel):
    latitude: float
    longitude: float

# Recycling Item Schema
class RecyclingItemCreate(BaseModel):
    material_type: str  # e.g., "plastic poles", "recycled tiles"
    quantity_available: float
    location: LocationCoordinates