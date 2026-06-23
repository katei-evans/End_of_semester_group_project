from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import producers, matching, recycling, analytics

app = FastAPI(
    title="EcoMarketplace API",
    description="Centralized digital hub for green energy and circular economy products.",
    version="1.0.0"
)

# Allow frontend applications (web/mobile) to connect to the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include feature-specific routers
app.include_router(producers.router, prefix="/api/producers", tags=["Producer Dashboard"])
app.include_router(matching.router, prefix="/api/matching", tags=["Geo-Location Matching"])
app.include_router(recycling.router, prefix="/api/recycling", tags=["Recycling Marketplace"])
app.include_router(analytics.router, prefix="/api/analytics", tags=["Analytics & Education"])

@app.get("/")
async def root():
    return {"message": "Welcome to the EcoMarketplace SDG 7 API Platform"}