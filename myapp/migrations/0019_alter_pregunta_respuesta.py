# Generated by Django 5.0.3 on 2025-03-28 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_pregunta_usuario_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='respuesta',
            field=models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8')]),
        ),
    ]
