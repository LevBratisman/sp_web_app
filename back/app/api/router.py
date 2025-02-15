from fastapi import APIRouter

from app.api.endpoints.member_controller import router as member_router
from app.api.endpoints.post_controller import router as post_router
from app.api.endpoints.date_controller import router as date_router

app_router = APIRouter()

app_router.include_router(post_router, prefix="/posts", tags=["Posts"])
app_router.include_router(member_router, prefix="/members", tags=["Members"])
app_router.include_router(date_router, prefix="/dates", tags=["Dates"])
