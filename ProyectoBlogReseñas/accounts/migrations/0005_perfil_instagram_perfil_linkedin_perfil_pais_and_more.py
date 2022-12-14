# Generated by Django 4.0.6 on 2022-09-26 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_perfil_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='pais',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='perfil',
            name='profesion',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
    ]
