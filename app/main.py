from fastapi import FastAPI
from app.routers import objects, service_info

app = FastAPI(
    title="Data Repository Service",
    version="1.4.0",
    description="The Data Repository Service (DRS) API provides a generic interface to data repositories.",
)

# Include routers
app.include_router(service_info.router)
app.include_router(objects.router)