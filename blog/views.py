#-*- coding:utf8 -*-
from django.shortcuts import render
from django.http import HttpResponse

#读取数据库的数据
from .models import Article,Author
#首页
def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    context = {'latest_article_list':latest_article_list}
    return render(request,"blog/index.html",context)

def articledetail(request,article_id):
    return HttpResponse("This is the detail of article")

def articlelist(request):
    return HttpResponse("This is the list of article")


# Create your views here.
