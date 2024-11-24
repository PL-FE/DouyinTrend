from tortoise import fields

from app.schemas.menus import MenuType

from .base import BaseModel, TimestampMixin
from .enums import MethodType


class User(BaseModel, TimestampMixin):
    username = fields.CharField(max_length=20, unique=True, description="用户名称", index=True)
    alias = fields.CharField(max_length=30, null=True, description="姓名", index=True)
    email = fields.CharField(max_length=255, unique=True, description="邮箱", index=True)
    phone = fields.CharField(max_length=20, null=True, description="电话", index=True)
    password = fields.CharField(max_length=128, null=True, description="密码")
    is_active = fields.BooleanField(default=True, description="是否激活", index=True)
    is_superuser = fields.BooleanField(default=False, description="是否为超级管理员", index=True)
    last_login = fields.DatetimeField(null=True, description="最后登录时间", index=True)
    roles = fields.ManyToManyField("models.Role", related_name="user_roles")
    dept_id = fields.IntField(null=True, description="部门ID", index=True)

    class Meta:
        table = "user"


class Role(BaseModel, TimestampMixin):
    name = fields.CharField(max_length=20, unique=True, description="角色名称", index=True)
    desc = fields.CharField(max_length=500, null=True, description="角色描述")
    menus = fields.ManyToManyField("models.Menu", related_name="role_menus")
    apis = fields.ManyToManyField("models.Api", related_name="role_apis")

    class Meta:
        table = "role"


class Api(BaseModel, TimestampMixin):
    path = fields.CharField(max_length=100, description="API路径", index=True)
    method = fields.CharEnumField(MethodType, description="请求方法", index=True)
    summary = fields.CharField(max_length=500, description="请求简介", index=True)
    tags = fields.CharField(max_length=100, description="API标签", index=True)

    class Meta:
        table = "api"


class Menu(BaseModel, TimestampMixin):
    name = fields.CharField(max_length=20, description="菜单名称", index=True)
    remark = fields.JSONField(null=True, description="保留字段")
    menu_type = fields.CharEnumField(MenuType, null=True, description="菜单类型")
    icon = fields.CharField(max_length=100, null=True, description="菜单图标")
    path = fields.CharField(max_length=100, description="菜单路径", index=True)
    order = fields.IntField(default=0, description="排序", index=True)
    parent_id = fields.IntField(default=0, max_length=10, description="父菜单ID", index=True)
    is_hidden = fields.BooleanField(default=False, description="是否隐藏")
    component = fields.CharField(max_length=100, description="组件")
    keepalive = fields.BooleanField(default=True, description="存活")
    redirect = fields.CharField(max_length=100, null=True, description="重定向")

    class Meta:
        table = "menu"


class Dept(BaseModel, TimestampMixin):
    name = fields.CharField(max_length=20, unique=True, description="部门名称", index=True)
    desc = fields.CharField(max_length=500, null=True, description="备注")
    is_deleted = fields.BooleanField(default=False, description="软删除标记", index=True)
    order = fields.IntField(default=0, description="排序", index=True)
    parent_id = fields.IntField(default=0, max_length=10, description="父部门ID", index=True)

    class Meta:
        table = "dept"


class DeptClosure(BaseModel, TimestampMixin):
    ancestor = fields.IntField(description="父代", index=True)
    descendant = fields.IntField(description="子代", index=True)
    level = fields.IntField(default=0, description="深度", index=True)


class AuditLog(BaseModel, TimestampMixin):
    user_id = fields.IntField(description="用户ID", index=True)
    username = fields.CharField(max_length=64, default="", description="用户名称", index=True)
    module = fields.CharField(max_length=64, default="", description="功能模块", index=True)
    summary = fields.CharField(max_length=128, default="", description="请求描述", index=True)
    method = fields.CharField(max_length=10, default="", description="请求方法", index=True)
    path = fields.CharField(max_length=255, default="", description="请求路径", index=True)
    status = fields.IntField(default=-1, description="状态码", index=True)
    response_time = fields.IntField(default=0, description="响应时间(单位ms)", index=True)


class DyVideoModel(BaseModel, TimestampMixin):
    video_id = fields.BigIntField(description="视频id", unique=True, )
    name = fields.CharField(max_length=255, description="博主")
    dy_user_id = fields.CharField(max_length=255, description="抖音用户id")
    video_url = fields.CharField(max_length=500, description="视频URL")
    download_url = fields.CharField(max_length=500, null=True, description="下载URL")
    title = fields.CharField(max_length=255, null=True, description="标题")
    tags = fields.CharField(max_length=255, null=True, description="视频标签")
    type = fields.CharField(max_length=50, null=True, description="类型")
    comment_count = fields.IntField(default=0, description="评论数")
    share_count = fields.IntField(default=0, description="分享数")
    like_count = fields.IntField(default=0, description="喜欢数")
    favorite_count = fields.IntField(default=0, description="收藏数")
    duration = fields.IntField(default=0, description="视频时长")
    publish_time = fields.DatetimeField(description="发布时间")
    text_recognition = fields.TextField(null=True, description="文本识别")
    remarks = fields.TextField(null=True, description="备注")
    created_at = fields.DatetimeField(auto_now_add=True, description="创建时间")
    updated_at = fields.DatetimeField(auto_now=True, description="更新时间")

    class Meta:
        table = "dyvideo"
