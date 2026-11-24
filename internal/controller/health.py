import time
from fastapi import APIRouter
from internal.config import settings

router = APIRouter()
START_TIME = time.time()

@router.get("/api/v1/health")
async def health_check():
    return {
        "status": "pass",
        "app_name": settings.app_name,
        "version": settings.app_version,
        "environment": settings.app_env,
        "uptime": round(time.time() - START_TIME)
    }
