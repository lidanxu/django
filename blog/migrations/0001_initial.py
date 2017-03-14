# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_title', models.CharField(max_length=20)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('Article_tag', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nickname', models.CharField(max_length=20)),
                ('birth', models.DateTimeField()),
                ('edu', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(to='blog.Author'),
        ),
    ]
