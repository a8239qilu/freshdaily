# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gtitle', models.CharField(max_length=20)),
                ('gprice', models.DecimalField(max_digits=5, decimal_places=2)),
                ('gunit', models.CharField(default=b'500g', max_length=20)),
                ('ginfo', models.CharField(max_length=200)),
                ('gpic', models.ImageField(upload_to=b'df_goods')),
                ('gclick', models.IntegerField()),
                ('gcontent', tinymce.models.HTMLField()),
                ('gstore', models.IntegerField()),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ttitle', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(to='df_goods.TypeInfo'),
        ),
    ]
