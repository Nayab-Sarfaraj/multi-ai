import logging
import os
from app.config.settings import settings
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.auth_router import router as auth_router
from app.routers.health_router import router as health_router



logger = logging.getLogger(__name__)

app = FastAPI(
    title=settings.app_name,
    version="0.0.1",
    description="Starter multi-agent backend with auth, Redis memory, Elasticsearch search, and router-based modular structure."
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.backend_cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(auth_router)


logger.info(
    "Application startup configured.",
    extra={
        "app_name": settings.app_name,
        "api_prefix": settings.api_prefix,
        "llm_provider": settings.llm_provider,
        "elastic_index": settings.elasticsearch_index,
    },
)