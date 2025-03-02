from fastapi import APIRouter

from app.api.v1.endpoints import auth, links, shared_links, users

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["Users"])
api_router.include_router(auth.router, prefix="/auth", tags=["Auth"])
api_router.include_router(links.router, prefix="/links", tags=["Links"])
api_router.include_router(shared_links.router, prefix="/links", tags=["Shared Links"])
