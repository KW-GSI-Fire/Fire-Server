from fastapi import APIRouter

from . import status


# Router
router = APIRouter(
    prefix="/api",
    tags=["api"],
    # responses={404: {"description": "Not Found"}},
)

# Middlewares - Routers
router.include_router(status.router)
