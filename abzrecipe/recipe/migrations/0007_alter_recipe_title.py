# Generated by Django 4.2.7 on 2023-11-08 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0006_recipeingredient_quantity_alter_recipestep_content_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='title',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
