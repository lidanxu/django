#-*- coding:utf8 -*-
from django.db import models
from  django.utils import timezone
import datetime
#作者
#编辑器
from DjangoUeditor.models import UEditorField

class Author(models.Model):
    #昵称
    nickname = models.CharField(max_length=20)
    birth = models.DateTimeField()
    intro = models.CharField(max_length=300,default="简介")
    edu = models.CharField(max_length=100)
    def __unicode__(self):
        return self.nickname

#文章
class Article(models.Model):
    #标题
    article_title = models.CharField(max_length=20)
    #发布内容
   # article_text = models.CharField(max_length=10000,default="发布内容")
    article_text = UEditorField("发布内容",height=300,width=1000,default=u'',blank=True,imagePath="uploads/images/",toolbars="besttome",filePath="uploads/files/")
    #发布时间
    pub_date = models.DateTimeField('date published')
    #标签
    article_tag = models.CharField(max_length=20)
    #一个作者对应多篇文章
    author = models.ForeignKey(Author)
    #一天内发布的
    def was_published_recently(self):
        return self.pub_date >= timezone.now()-datetime.timedelta(days=1)
    #在列表中根据pub_date排序
    was_published_recently.admin_order_field='pub_date'
    #列表中显示的数据类型
    was_published_recently.boolean = True
    #列表中的标签
    was_published_recently.short_description = 'Published recently '

    def __unicode__(self):
        return self.article_title

