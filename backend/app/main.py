from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from .core.config import settings
from .core.exceptions import global_exception_handler, ai_provider_exception_handler, AIProviderUnavailableError
from .api.v1 import copilot, scenarios, incidents, approvals

limiter = Limiter(key_func=get_remote_address, default_limits=["5/minute"])

app = FastAPI(title=settings.PROJECT_NAME)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.add_exception_handler(Exception, global_exception_handler)
app.add_exception_handler(AIProviderUnavailableError, ai_provider_exception_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(copilot.router, prefix=f"{settings.API_V1_STR}/copilot")
app.include_router(scenarios.router, prefix=f"{settings.API_V1_STR}/scenarios")
app.include_router(incidents.router, prefix=f"{settings.API_V1_STR}/incidents")
app.include_router(approvals.router, prefix=f"{settings.API_V1_STR}/approvals")
