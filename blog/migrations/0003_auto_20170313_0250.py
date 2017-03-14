# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170313_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_text',
            field=models.CharField(default=b'\xe5\x8f\x91\xe5\xb8\x83\xe5\x86\x85\xe5\xae\xb9', max_length=10000),
        ),
        migrations.AlterField(
            model_name='author',
            name='intro',
            field=models.CharField(default=b'\xe7\xae\x80\xe4\xbb\x8b', max_length=300),
        ),
    ]
