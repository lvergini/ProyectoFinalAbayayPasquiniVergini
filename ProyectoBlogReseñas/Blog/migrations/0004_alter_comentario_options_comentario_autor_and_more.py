# Generated by Django 4.0.6 on 2022-09-16 23:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Libros', '0001_initial'),
        ('Blog', '0003_alter_post_cuerpo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={'ordering': ['fecha_comentario']},
        ),
        migrations.AddField(
            model_name='comentario',
            name='autor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comentario',
            name='comentario',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='comentario',
            name='fecha_comentario',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='comentario',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='Blog.post'),
        ),
        migrations.AddField(
            model_name='post',
            name='libro',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Libros.libro'),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='fecha_publicacion',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
