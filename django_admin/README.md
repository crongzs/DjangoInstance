# Django Admin 配置以及汉化

### admin配置

**date_hierarchy**
根据你指定的日期相关的字段，为页面创建一个时间导航栏，可通过日期过滤对象

**empty_value_display**
指定空白显示的内容。如果你有些字段没有值（例如None，空字符串等等），默认情况下会显示破折号“-”。这个选项可以让你自定义显示什么

**fields**
按你希望的顺序，显示指定的字段。与exclude相对。

**exclude**
不显示指定的某些字段。

**list_select_related**
Django将会使用select_related()方法查询数据，这可能会帮助你减少一些数据库访问。只对ForeignKey字段调用select_related()方法。

**ordering**
排序

**list_display**
指定显示在修改页面上的字段。这是一个很常用也是最重要的技巧之一。

**list_display_links**
指定用于链接修改页面的字段。

**list_editable**
选项是让你指定在修改列表页面中哪些字段可以被编辑。指定的字段将显示为编辑框，可修改后直接批量保存

**form**
自定义form表单

**list_filter**
可以激活修改列表页面的右侧边栏，用于对列表元素进行过滤

**list_max_show_all**
设置一个数值，当列表元素总数小于这个值的时候，将显示一个“show all”链接，点击后就能看到一个展示了所有元素的页面。该值默认为200.

**list_per_page**
admin的修改列表页面添加一个搜索框。

**search_fields**
admin的修改列表页面添加一个搜索框。

### admin汉化

* settings.py 语言设置为zh-hans，时区设置为Asia/Shanghai
~~~python
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True
~~~

* 模型中表明和字段名设置`verbose_name`
~~~python
verbose_name = '建设单位'
verbose_name_plural = verbose_name
~~~

* 给app设置`verbose_name`
myapp/apps.py
~~~python
from django.apps import AppConfig


class MyappConfig(AppConfig):
    name = 'myapp'
    verbose_name = '测绘'
~~~
myapp/__init__.py
~~~python
default_app_config = 'myapp.apps.MyappConfig'
~~~

* 修改标题
重新编写django-admin后台页面html模版，覆盖源码模版
templates/admin/base_site.html
~~~html
{% extends "admin/base.html" %}

{% block title %}{{ title }} | 后台{% endblock %}

{% block branding %}

<h1 id="site-name"><a href="{% url 'admin:index' %}">后台</a></h1>
{% endblock %}

{% block nav-global %}{% endblock %}
~~~