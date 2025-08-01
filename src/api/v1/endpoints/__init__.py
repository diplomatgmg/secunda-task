from fastapi import APIRouter

from api.v1.endpoints import activity, building


__all__ = ["router"]


router = APIRouter()
router.include_router(building.router, prefix="/buildings", tags=["buildings"])
router.include_router(activity.router, prefix="/activities", tags=["activities"])
