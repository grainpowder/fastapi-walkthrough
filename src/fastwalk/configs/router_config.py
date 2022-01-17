from fastapi import APIRouter
from fastwalk.routers import (arithmetic, algebra, ping)

router = APIRouter()
router.include_router(ping.router)
router.include_router(arithmetic.router)
router.include_router(algebra.router)
