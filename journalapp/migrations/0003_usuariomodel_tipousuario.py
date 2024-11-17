# Generated by Django 5.1.3 on 2024-11-17 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalapp', '0002_usuariomodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuariomodel',
            name='tipoUsuario',
            field=models.CharField(choices=[('ADMIN', 'ADMIN'), ('USER', 'USER')], db_column='tipo_usuario', default='ADMIN', max_length=100),
        ),
    ]
