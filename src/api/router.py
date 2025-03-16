from fastapi import APIRouter

from src.api.reservations import router as reservations_router

router = APIRouter(prefix='/api/v1')
router.include_router(reservations_router)
