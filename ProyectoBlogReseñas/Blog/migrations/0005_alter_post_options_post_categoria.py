# Generated by Django 4.0.6 on 2022-09-17 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_alter_comentario_options_comentario_autor_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-fecha_publicacion']},
        ),
        migrations.AddField(
            model_name='post',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Blog.categoria'),
        ),
    ]
