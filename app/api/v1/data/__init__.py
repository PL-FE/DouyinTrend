from fastapi import APIRouter

from .data import router

data_router = APIRouter()
data_router.include_router(router, tags=["数据模块"])

__all__ = ["data_router"]
