# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockTable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('open', models.DecimalField(max_digits=5, decimal_places=2)),
                ('high', models.DecimalField(max_digits=5, decimal_places=2)),
                ('low', models.DecimalField(max_digits=5, decimal_places=2)),
                ('close', models.DecimalField(max_digits=5, decimal_places=2)),
            ],
        ),
    ]
