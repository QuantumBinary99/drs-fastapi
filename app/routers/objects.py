from fastapi import APIRouter, Path, HTTPException
from app.models import DrsObject, AccessURL
from datetime import datetime

router = APIRouter()

@router.get("/objects/{object_id}", response_model=DrsObject)
async def get_object(object_id: str = Path(..., description="DRS object identifier")):
    if object_id == "314159":
        return {
            "id": "314159",
            "self_uri": "drs://drs.example.org/314159",
            "size": 1024,
            "created_time": datetime.now(),
            "checksums": [{"checksum": "72794b6d", "type": "md5"}],
            "name": "example_object",
            "updated_time": datetime.now(),
            "version": "1.0.0",
            "mime_type": "application/octet-stream",
            "access_methods": [{"type": "https", "access_url": {"url": "https://drs.example.org/314159"}}],
            "contents": [],  # Empty list for contents (not a bundle)
            "description": "An example DRS object",
            "aliases": ["example_alias"],
        }
    else:
        raise HTTPException(status_code=404, detail="Object not found")

@router.get("/objects/{object_id}/access/{access_id}", response_model=AccessURL)
async def get_access_url(object_id: str, access_id: str):
    if object_id == "314159" and access_id == "access123":
        return {"url": "https://drs.example.org/314159", "headers": ["Authorization: Basic Z2E0Z2g6ZHJz"]}
    else:
        raise HTTPException(status_code=404, detail="Access URL not found")