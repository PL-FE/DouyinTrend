from typing import Any, Dict, Generic, List, NewType, Tuple, Type, TypeVar, Union

from pydantic import BaseModel
from tortoise.expressions import Q
from tortoise.models import Model
from tortoise.transactions import in_transaction

Total = NewType("Total", int)
ModelType = TypeVar("ModelType", bound=Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get(self, id: int) -> ModelType:
        return await self.model.get(id=id)

    async def list(self, page: int, page_size: int, search: Q = Q(), order: list = []) -> Tuple[Total, List[ModelType]]:
        query = self.model.filter(search)
        return await query.count(), await query.offset((page - 1) * page_size).limit(page_size).order_by(*order)

    async def create(self, obj_in: CreateSchemaType) -> ModelType:
        if isinstance(obj_in, Dict):
            obj_dict = obj_in
        else:
            obj_dict = obj_in.model_dump()
        obj = self.model(**obj_dict)
        await obj.save()
        return obj

    async def update(self, id: int, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> ModelType:
        if isinstance(obj_in, Dict):
            obj_dict = obj_in
        else:
            obj_dict = obj_in.model_dump(exclude_unset=True, exclude={"id"})
        obj = await self.get(id=id)
        obj = obj.update_from_dict(obj_dict)
        await obj.save()
        return obj

    async def remove(self, id: int) -> None:
        obj = await self.get(id=id)
        await obj.delete()

    # async def bulk_create(self, objs_in: List[Union[CreateSchemaType, Dict[str, Any]]]) -> List[ModelType]:
    #     # 准备要创建的对象列表
    #     objs_to_create = []
    #
    #     for obj_in in objs_in:
    #         if isinstance(obj_in, Dict):
    #             obj_dict = obj_in
    #         else:
    #             obj_dict = obj_in.model_dump(exclude_unset=True)
    #         obj = self.model(**obj_dict)
    #         objs_to_create.append(obj)
    #
    #     # 使用事务批量创建对象
    #     async with in_transaction():
    #         await self.model.bulk_create(objs_to_create)
    #
    #     return objs_to_create
    #
    # async def bulk_update(self, objs_in: List[Union[UpdateSchemaType, Dict[str, Any]]]) -> List[ModelType]:
    #     # 准备要更新的对象列表
    #     updated_objs = []
    #
    #     for obj_in in objs_in:
    #         if isinstance(obj_in, Dict):
    #             obj_dict = obj_in
    #         else:
    #             obj_dict = obj_in.model_dump(exclude_unset=True, exclude={"id"})
    #         obj = await self.get(id=obj_dict["id"])
    #         obj = obj.update_from_dict(obj_dict)
    #         updated_objs.append(obj)
    #
    #     # 使用事务批量更新对象
    #     async with in_transaction():
    #         for obj in updated_objs:
    #             await obj.save()
    #
    #     return updated_objs
