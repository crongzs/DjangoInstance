# Django 跨域
浏览器因为同源策略拒绝向非同域的请求返回数据
* 同源：ip地址和端口号都相同才是同一个域

### 解决方法一：自定义中间件

~~~python
class MyCorsMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Access-Control-Allow-Origin'] = '*'
        return response
~~~

settings.py
~~~python
MIDDLEWARE = [
    ...
    'myapp.middlewares.MyCorsMiddleware'
]
~~~

### 解决方法二：使用django-cors-headers

~~~bash
pip install django-cors-headers
~~~

settings.py
~~~python
INSTALLED_APPS = [
    ...
    'corsheaders'
]

MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]

# 跨域 cors-origin配置
# 白名单
CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000"
]

CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]

CORS_ALLOW_HEADERS = [
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
]
~~~