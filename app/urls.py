from django.conf.urls import url
from . import views  # .表示在本目录下引用views.py
from django.urls import path

urlpatterns = [
    url('login', views.index),
    url('showAll', views.show_all),
    url('addUser', views.add_user),
    url('to_add', views.to_add),
    url('del', views.del_user),
    url('to_modify', views.to_modify),
    url('modify', views.modify_user),
    url(r'', views.index, name='first-url'),
]

'''
解释：
	第一行代码引入了django.conf.urls中的url()函数，因为Django中的所有路由映射由该函数生成。
	第二行代码引入了djangosite/app/views.py模块。
	定义了关键变量urlpatterns，该变量是一个列表，保存所有由url()函数生成的路由映射。
	url(r'', views.index, name='first-url')表示：
		把所有路由映射到views.py的index函数中，并把该映射命名为first-url。
'''
