# Generated by Django 4.2.7 on 2023-11-06 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_alter_recipestep_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='title',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
