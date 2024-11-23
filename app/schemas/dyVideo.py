from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class BaseDyVideo(BaseModel):
    video_id: int
    name: str
    video_url: str = ""
    download_url: str = ""
    title: str = ""
    tags: str = ""
    type: str = ""
    comment_count: int = 0
    share_count: int = 0
    like_count: int = 0
    favorite_count: int = 0
    duration: int = 0
    publish_time: datetime
    text_recognition: str
    remarks: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class DyVideoCreate(BaseModel):
    video_id: int = Field(example='视频id')
    name: str = Field(example='博主名称')
    video_url: str = Field(example='视频url')
    download_url: str = Field(example='下载url')
    title: str = Field(example='标题')
    tags: str = Field(example='标签')
    type: str = Field(example='类型')
    comment_count: int = Field(0, example="评论数")
    share_count: int = Field(0, example="分享数")
    like_count: int = Field(0, example="喜欢数")
    favorite_count: int = Field(0, example="收藏数")
    duration: int = Field(0, example="视频时长")
    publish_time: datetime = Field(example='发布时间')
    text_recognition: str = Field(example='文本识别')
    remarks: str = Field(example='备注')


class DyVideoUpdate(BaseModel):
    id: int
    video_id: int = Field(example='视频id')
    name: str = Field(example='博主名称')
    video_url: str = Field(example='视频url')
    download_url: str = Field(example='下载url')
    title: str = Field(example='标题')
    tags: str = Field(example='标签')
    type: str = Field(example='类型')
    comment_count: int = Field(0, example="评论数")
    share_count: int = Field(0, example="分享数")
    like_count: int = Field(0, example="喜欢数")
    favorite_count: int = Field(0, example="收藏数")
    duration: int = Field(0, example="视频时长")
    publish_time: datetime = Field(example='发布时间')
    text_recognition: str = Field(example='文本识别')
    remarks: str = Field(example='备注')

    def update_dict(self):
        return self.model_dump(exclude_unset=True, exclude={"id", "video_id"})
