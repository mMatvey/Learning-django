# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-25 06:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Краткое описание')),
                ('in_stock', models.BooleanField(db_index=True, default=True, verbose_name='Есть в наличии')),
                ('price', models.FloatField(db_index=True, verbose_name='Цена руб.')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='page.Category', verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'товары',
                'ordering': ['-price', 'name'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='good',
            unique_together=set([('category', 'name', 'price')]),
        ),
    ]