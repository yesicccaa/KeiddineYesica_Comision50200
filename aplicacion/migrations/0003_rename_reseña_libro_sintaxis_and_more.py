# Generated by Django 5.0.1 on 2024-02-07 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0002_autor_libro'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='reseña',
            new_name='sintaxis',
        ),
        migrations.RemoveField(
            model_name='libro',
            name='fecha_publicacion',
        ),
        migrations.AddField(
            model_name='libro',
            name='año_publicacion',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
