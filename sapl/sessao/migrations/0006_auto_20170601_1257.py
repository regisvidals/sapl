# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-06-01 12:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sessao', '0005_auto_20170601_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='votonominal',
            name='votacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sessao.RegistroVotacao'),
        ),
        migrations.AlterField(
            model_name='votoparlamentar',
            name='votacao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sessao.RegistroVotacao'),
        ),
    ]
