from fastapi import APIRouter
from app.models import DrsService
from datetime import datetime

router = APIRouter()

@router.get("/service-info", response_model=DrsService)
async def get_service_info():
    return {
        "id": "com.example.drs",
        "name": "Example DRS API",
        "type": {"group": "org.ga4gh", "artifact": "drs", "version": "1.4.0"},
        "description": "Serves data according to DRS specification",
        "organization": {"name": "Example Company", "url": "https://example.com"},
        "contactUrl": "mailto:support@example.com",
        "documentationUrl": "https://docs.example.com/docs/drs",
        "createdAt": datetime.now(),
        "updatedAt": datetime.now(),
        "environment": "production",
        "version": "1.13.4",
        "maxBulkRequestLength": 100,
    }