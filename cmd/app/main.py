import uvicorn
from fastapi import FastAPI
from internal.controller.health import router
from internal.config import settings

app = FastAPI(title=settings.app_name, version=settings.app_version)
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=settings.http_port)
