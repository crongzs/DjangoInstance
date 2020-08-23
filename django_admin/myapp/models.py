from datetime import timezone
import uuid
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User, Group


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    del_states = models.BooleanField('已删除', default=False)

    class Meta:
        abstract = True


# 建设单位
class BuildUnit(BaseModel):
    id = models.UUIDField("id", primary_key=True, default=uuid.uuid4)
    name = models.CharField('单位名称', max_length=200)
    code = models.CharField('统一社会信用代码', max_length=20, unique=True, default='')
    contact_person = models.CharField('联系人', max_length=20)
    phone = models.CharField('联系电话', max_length=50, blank=True, null=True)
    address = models.CharField('单位地址', max_length=128, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'build_unit'
        verbose_name = '建设单位'
        verbose_name_plural = verbose_name


# 联测机构
class MappingOrgan(BaseModel):
    id = models.UUIDField("id", primary_key=True, default=uuid.uuid4)
    code = models.CharField('统一社会信用代码', max_length=18, unique=True)
    name = models.CharField('企业名称', max_length=100)
    representative = models.CharField('法人', max_length=100)
    type = models.CharField('单位性质', max_length=100)
    fund = models.IntegerField('注册资本', default=0)
    ts_public = models.DateField('注册时间', null=True, blank=True)
    scope = models.TextField('经营范围', null=True, blank=True)
    address = models.CharField('单位地址', max_length=200)
    contact_person = models.CharField('联系人', max_length=20)
    contact_phone = models.CharField('联系电话', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'mapping_organ'
        verbose_name = '联测机构'
        verbose_name_plural = verbose_name


# 测绘项目
class Project(BaseModel):
    id = models.UUIDField("id", primary_key=True, default=uuid.uuid4)
    unit = models.ForeignKey(BuildUnit, related_name='p_bunit', on_delete=CASCADE, blank=True, null=True)
    mappingorgan = models.ForeignKey(MappingOrgan, related_name='mappingorgan', on_delete=CASCADE, blank=True,
                                     null=True)
    name = models.CharField('项目名称', max_length=128)
    type = models.CharField('项目类型', max_length=20)
    code = models.CharField('统一代码', max_length=200, unique=True)
    source = models.CharField('来源token', max_length=200)
    # state: 1申请测绘2已委托3接受委托正在测绘4拒绝委托5成果提交并入档
    state = models.IntegerField('项目状态', default=1)
    addr = models.CharField('项目地址', max_length=500)
    contact_person = models.CharField('联系人', max_length=20)
    contact_phone = models.CharField('联系电话', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'project'
        verbose_name = '测绘项目'
        verbose_name_plural = verbose_name
        unique_together = ['code', 'unit', 'mappingorgan']
