from fastapi import APIRouter, Query, Body

from app.schemas import Success

# from app.controllers.dept import dept_controller
# from app.schemas import Success
# from app.schemas.depts import *
from app.controllers.dy import dy_controller

router = APIRouter()


@router.post("/crawl/dy/video", summary="爬取抖音视频数据")
# 获取 urls 入参：['','']
async def list_dept(
        urls: list[str] = Body(..., description="urls")
):
    await dy_controller.run_task(urls)
    return Success(msg="Created Successfully")
