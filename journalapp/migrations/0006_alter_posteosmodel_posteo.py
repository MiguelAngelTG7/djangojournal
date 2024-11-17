# Generated by Django 5.1.3 on 2024-11-17 06:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalapp', '0005_posteosmodel_posteo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteosmodel',
            name='posteo',
            field=models.ForeignKey(db_column='posteo_id', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
