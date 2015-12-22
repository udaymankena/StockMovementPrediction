# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0002_stocktable'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocktable',
            name='company',
            field=models.CharField(default=b'Apple', max_length=50),
        ),
    ]
