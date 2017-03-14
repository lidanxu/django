# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170313_0250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='Article_tag',
            new_name='article_tag',
        ),
    ]
