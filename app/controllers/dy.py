from datetime import datetime
from typing import List

from app.core.crud import CRUDBase
from app.models.admin import DyVideoModel
from app.schemas.dyVideo import DyVideoCreate, DyVideoUpdate
from app.spiders.dy_video.dy import Douyin


class DyController(CRUDBase[DyVideoModel, DyVideoCreate, DyVideoUpdate]):
    def __init__(self):
        super().__init__(model=DyVideoModel)

    async def run_task(self, urls):
        douyin = Douyin()
        data = douyin.inits(urls)
        print(data)
        await self.bulk_update_or_create(data)

        # async def bulk_upsert(self, objs_in: List[Union[CreateSchemaType, Dict[str, Any]]]) -> List[ModelType]:

    async def bulk_update_or_create(self, videos: List[dict]):

        # 提取所有 video_id 并转换为集合
        existing_video_ids = {int(video["video_id"]) for video in videos}

        # 查询现有的 video_id 并转换为集合
        existing_videos = set(
            await self.model.filter(video_id__in=existing_video_ids).values_list("video_id", flat=True))

        # 新增的记录
        new_videos = [video for video in videos if int(video["video_id"]) not in existing_videos]

        # 更新的记录
        update_videos = [video for video in videos if int(video["video_id"]) in existing_videos]

        if new_videos:
            # 执行新增操作
            await self.model.bulk_create([
                self.model(**video) for video in new_videos
            ], skip_duplicates=True)  # skip_duplicates=True 可以避免重复的 primary key 错误

        # 执行更新操作
        if update_videos:
            update_objects = []
            for video in update_videos:
                existing_video = await self.model.get(video_id=video["video_id"])
                existing_video.id = video["id"]
                existing_video.comment_count = video["comment_count"]
                existing_video.share_count = video["share_count"]
                existing_video.like_count = video["like_count"]
                existing_video.favorite_count = video["favorite_count"]
                update_objects.append(existing_video)

            await self.model.bulk_update(update_objects,
                                         fields=["comment_count", "share_count", "like_count", "favorite_count"])


dy_controller = DyController()
