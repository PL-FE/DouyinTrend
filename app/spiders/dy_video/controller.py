
from app.core.crud import CRUDBase
from app.models.admin import DyVideo
from  app.spiders.dy_video.schema import DyCreate, DyUpdate

class DyController(CRUDBase[DyVideo, DyCreate, DyUpdate]):
    def __init__(self):
        super().__init__(model=DyVideo)


dy_controller = DyController()
