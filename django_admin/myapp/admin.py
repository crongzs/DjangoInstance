from django.contrib import admin
from django import forms

# Register your models here.

from myapp.models import Project, BuildUnit, MappingOrgan


class ProjectModelAdmin(admin.ModelAdmin):
    # 根据你指定的日期相关的字段，为页面创建一个时间导航栏，可通过日期过滤对象
    date_hierarchy = 'create_time'
    # 指定空白显示的内容。如果你有些字段没有值（例如None，空字符串等等），默认情况下会显示破折号“-”。这个选项可以让你自定义显示什么，如下例就显示为“-empty-”：
    empty_value_display = '-empty-'
    # 按你希望的顺序，显示指定的字段。与exclude相对。
    fields = (('name', 'type'), ('code', 'state',), ('unit', 'mappingorgan'), 'addr')  # ('name', 'type'), 让name和type同行显示
    # Django将会使用select_related()方法查询数据，这可能会帮助你减少一些数据库访问。只对ForeignKey字段调用select_related()方法。
    list_select_related = ['unit', 'mappingorgan']
    # 排序
    ordering = ['create_time']


@admin.register(BuildUnit)
class BuildUnitModelAdmin(admin.ModelAdmin):
    # 指定显示在修改页面上的字段。这是一个很常用也是最重要的技巧之一。
    list_display = ['name', 'code', 'phone', 'address']
    # 指定用于链接修改页面的字段。
    list_display_links = ('name', 'code')
    # list_display_links = None 如果设置为None，则根本没有链接了，你无法跳到目标的修改页面。
    # 选项是让你指定在修改列表页面中哪些字段可以被编辑。指定的字段将显示为编辑框，可修改后直接批量保存
    list_editable = ['address']


class MappingOrganForm(forms.ModelForm):
    class Meta:
        model = MappingOrgan
        fields = ['name', 'code', 'type', 'fund', 'representative']


@admin.register(MappingOrgan)
class MappingOrganModelAdmin(admin.ModelAdmin):
    # 不显示指定的某些字段。
    exclude = ('id',)
    # 自定义form表单
    form = MappingOrganForm
    # 可以激活修改列表页面的右侧边栏，用于对列表元素进行过滤
    list_filter = ('type', 'scope')
    # 设置一个数值，当列表元素总数小于这个值的时候，将显示一个“show all”链接，点击后就能看到一个展示了所有元素的页面。该值默认为200.
    list_max_show_all = 20
    # 置每页显示多少个元素。Django自动帮你分页。默认为100。
    list_per_page = 10
    # admin的修改列表页面添加一个搜索框。
    search_fields = ['name', 'code']


admin.site.register(Project, ProjectModelAdmin)
