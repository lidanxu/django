# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_text',
            field=models.CharField(default=None, max_length=10000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='intro',
            field=models.CharField(default=None, max_length=300),
            preserve_default=False,
        ),
    ]
