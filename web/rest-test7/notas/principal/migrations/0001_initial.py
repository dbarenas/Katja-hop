# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('indentifier', models.IntegerField(default=0)),
                ('GPS_coordinates', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('site_category', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('track', models.IntegerField(default=0)),
                ('producer', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('rating', models.IntegerField(default=0)),
                ('classification', models.CharField(max_length=100)),
                ('atype', models.CharField(max_length=100)),
                ('date_recorded', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('identifier', models.CharField(max_length=10)),
                ('background_image', models.CharField(max_length=100)),
                ('deleted', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
