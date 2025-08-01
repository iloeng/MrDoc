# coding:utf-8
# @文件: serializers_app.py
# @创建者：州的先生
# #日期：2020/5/11
# 博客地址：zmister.com

from rest_framework import serializers
from rest_framework.serializers import ModelSerializer,SerializerMethodField
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from app_doc.models import *
from app_admin.models import RegisterCode


# 用户序列化器
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
                'id', 'last_login', 'is_superuser', 'username', 'email', 'date_joined', 'is_active', 'first_name'
            )

# 注册邀请码序列化器
class RegisterCodeSerializer(ModelSerializer):
    status = serializers.SerializerMethodField(label="状态")

    class Meta:
        model = RegisterCode
        fields = ('__all__')

    def get_status(self,obj):
        current_date = timezone.now().date()
        if obj.used_cnt >= obj.all_cnt:
            return _('使用次数已满')
        elif obj.expire_date is not None and obj.expire_date < current_date:
            return _('已到期')
        else:
            return _('有效')

# 文集序列化器
class ProjectSerializer(ModelSerializer):
    create_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M')
    doc_total = serializers.SerializerMethodField(label="文档数")
    username = serializers.SerializerMethodField(label="作者")

    class Meta:
        model = Project
        fields = ('__all__')

    def get_username(self,obj):
        return obj.create_user.username

    def get_doc_total(self,obj):
        return Doc.objects.filter(top_doc=obj.id).count()

# 协作文集序列化器
class ProjectCollaSerializer(ModelSerializer):
    project_id = serializers.SerializerMethodField(label="文集ID")
    project_name = serializers.SerializerMethodField(label="文集名称")
    username = serializers.SerializerMethodField(label='文集创建人')
    top_doc = serializers.SerializerMethodField(label="上级")

    class Meta:
        model = ProjectCollaborator
        fields = ('__all__')

    def get_project_name(self,obj):
        return obj.project.name

    def get_project_id(self,obj):
        return obj.project.id

    def get_username(self,obj):
        username = obj.project.create_user.username
        return username

    def get_top_doc(self,obj):
        return 0


# 文档序列化器
class DocSerializer(ModelSerializer):

    project_name = SerializerMethodField(label="所属文集")
    modify_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    class Meta:
        model = Doc
        fields = ('__all__')

    # 返回文档的所属文集
    def get_project_name(self,obj):
        pro_name = Project.objects.get(id=obj.top_doc).name
        return pro_name


# 文档历史序列化器
class DocHistorySerializer(ModelSerializer):
    username = serializers.SerializerMethodField(label="用户名")
    class Meta:
        model = DocHistory
        fields = ('__all__')

    def get_username(self,obj):
        return obj.create_user.username


# 文档模板序列化器
class DocTempSerializer(ModelSerializer):
    class Meta:
        model = DocTemp
        fields = ('__all__')

# 图片序列化器
class ImageSerializer(ModelSerializer):
    username = serializers.SerializerMethodField(label="用户名")
    class Meta:
        model = Image
        fields = ('__all__')

    def get_username(self,obj):
        return obj.user.username

# 图片分组序列化器
class ImageGroupSerializer(ModelSerializer):
    class Meta:
        model = ImageGroup
        fields = ('__all__')

# 附件序列化器
class AttachmentSerializer(ModelSerializer):
    file_path = serializers.CharField()
    username = serializers.SerializerMethodField(label="用户名")

    class Meta:
        model = Attachment
        fields = ('__all__')

    def get_username(self,obj):
        return obj.user.username
