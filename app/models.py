from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class ServiceType(BaseModel):
    group: str
    artifact: str
    version: str

class Service(BaseModel):
    id: str
    name: str
    type: ServiceType
    description: str
    organization: dict
    contactUrl: str
    documentationUrl: str
    createdAt: datetime
    updatedAt: datetime
    environment: str
    version: str

class DrsService(Service):
    maxBulkRequestLength: int

class Checksum(BaseModel):
    checksum: str
    type: str

class AccessURL(BaseModel):
    url: str
    headers: Optional[List[str]]

class DrsObject(BaseModel):
    id: str
    self_uri: str
    size: int
    created_time: datetime
    checksums: List[Checksum]
    name: Optional[str]
    updated_time: Optional[datetime]
    version: Optional[str]
    mime_type: Optional[str]
    access_methods: Optional[List[dict]]
    contents: Optional[List[dict]]
    description: Optional[str]
    aliases: Optional[List[str]]