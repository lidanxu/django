#-*- coding:utf8 -*-
#应用目录创建URLconf，通过创建urls.py实现
from django.conf.urls import url
from . import views
urlpatterns = [
    # 首页
    url(r'^$',views.index,name='index'),
    url(r'^article/(?P<article_id>[0-9]+)/$',views.articledetail,name='articledetail'),
    url(r'^article/list/$',views.articlelist,name='articlelistn'),

]
