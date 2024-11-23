from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

class BaseRole(BaseModel):
    video_id: int
    name: str
    video_url: str = ""
    download_url: str = ""
    title: str = ""
    tags: str = ""
    type: str = ""
    comment_count: int = "0"
    share_count: int = "0"
    like_count: int = "0"
    favorite_count: int = "0"
    duration: int = "0"
    publish_time: datetime
    text_recognition: str
    remarks: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class DyCreate(BaseModel):
    ...

class DyUpdate(BaseModel):
    ...