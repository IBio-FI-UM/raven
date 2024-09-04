# Generated by Django 5.0.3 on 2024-04-23 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_imagen_imagen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=200)),
                ('genero', models.CharField(max_length=200)),
                ('facultad', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='imagen',
            name='opcion',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.AddField(
            model_name='pregunta',
            name='codigo',
            field=models.CharField(default='SOME STRING', max_length=200),
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
