from fastapi import APIRouter, Query, Body

from app.schemas import Success

# from app.controllers.dept import dept_controller
# from app.schemas import Success
# from app.schemas.depts import *
from app.controllers.dy import dy_controller
from app.schemas.dyVideo import claw_video_dy, ClawCommentsDySchemas

router = APIRouter()


@router.post("/crawl/dy/video", summary="爬取抖音视频数据")
# 获取 urls 入参：['','']
async def list_dept(data: claw_video_dy):
    await dy_controller.run_video_task(data.urls, data.cookie)
    return Success(msg="Created Successfully")


@router.post("/crawl/dy/comments", summary="爬取抖音视频的评论")
async def list_dept(data: ClawCommentsDySchemas):
    await dy_controller.run_comments_task(data.video_ids, data.cookie)
    return Success(msg="Created Successfully")
