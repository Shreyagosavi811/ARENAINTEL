from fastapi import Request
from fastapi.responses import JSONResponse
import logging

logger = logging.getLogger("stadiumops")

class AIProviderUnavailableError(Exception): pass

async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(status_code=500, content={"detail": "Internal Server Error"})

async def ai_provider_exception_handler(request: Request, exc: AIProviderUnavailableError):
    return JSONResponse(status_code=503, content={"detail": "AI service unavailable."})
