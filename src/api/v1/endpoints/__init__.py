from fastapi import APIRouter

from api.v1.endpoints import building


__all__ = ["router"]


router = APIRouter()
router.include_router(building.router, prefix="/buildings", tags=["buildings"])
