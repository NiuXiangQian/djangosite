from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf.urls import include

urlpatterns = [
    url(r'^app/', include('app.urls')),
    path('admin/', admin.site.urls),
]

'''
解释：
	首先通过import语句引入了django.conf.urls.include()函数；
	然后在urlpatterns列表中增加了一个路径app/，将其转接到app.urls包，即djangosite/app/urls.py文件。
	这样，通过include()函数就将两个urlpatterns连接起来了。
说明：
	可以看到这里的urlpatterns中既有url()函数，又有path()函数，
	两者的作用都是在urlpatterns中定义路由映射。
	它们的区别在于url()的第一个参数用正则表达式表达URL路由，
	而path()的第一个参数是普通字符串。
'''
