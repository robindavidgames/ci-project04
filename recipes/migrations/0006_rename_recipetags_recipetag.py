# Generated by Django 3.2 on 2022-07-08 12:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20220708_1207'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RecipeTags',
            new_name='RecipeTag',
        ),
    ]