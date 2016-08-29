# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contato', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefas',
            fields=[
                ('tarefa_id', models.AutoField(primary_key=True, serialize=False)),
                ('tarefa_nome', models.CharField(max_length=120)),
                ('tarefa_data_inico', models.DateField()),
                ('concluido', models.BooleanField(verbose_name='concluido')),
            ],
        ),
    ]
