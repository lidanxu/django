#-*- coding:utf8 -*-
from django.contrib import admin
from .models import Author,Article

# class ArticleInline(admin.TabularInline):
    # model = Article
    # extra = 3

class AuthorAdmin(admin.ModelAdmin):
    list_display=('nickname','intro')
    fieldsets =[
        (None,{'fields':['nickname','birth','edu']}),
        ('Introduce',{'fields':['intro']}),
    ]
    #inlines=[ArticleInline]
#自定义管理界面中表单的外观和功能
class ArticleAdmin(admin.ModelAdmin):
    list_display=('article_title','author','article_tag','pub_date','was_published_recently')
    # fields = ['article_title','author','article_text','pub_date','article_tag']
    fieldsets = [
        ('Article',{'fields':['article_title','author','article_text','article_tag']}),
        ('Date information',{'fields':['pub_date'],'classes':['collapse']}),#classes:collapse 使Date_information隐藏
    ]
    #下行代码添加一个’Filter'侧边栏，通过pub_date字段对变更列表进行过滤
    list_filter = ['pub_date']
    #添加搜索功能,在变更列表的顶部添加搜索框
    search_fields = ['article_title']
admin.site.register(Author,AuthorAdmin)
admin.site.register(Article,ArticleAdmin)
# Register your models here.
