# Generated by Django 5.0.3 on 2024-04-11 14:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_imagen_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagen',
            name='pregunta',
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta', models.CharField(max_length=200)),
                ('imagen', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.imagen')),
            ],
        ),
    ]
