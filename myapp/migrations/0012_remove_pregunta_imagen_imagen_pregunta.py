# Generated by Django 5.0.3 on 2024-05-15 12:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_remove_imagen_opcion_alter_pregunta_codigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pregunta',
            name='imagen',
        ),
        migrations.AddField(
            model_name='imagen',
            name='pregunta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.pregunta'),
        ),
    ]
