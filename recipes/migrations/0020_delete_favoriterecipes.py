# Generated by Django 3.1.4 on 2021-01-03 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0019_auto_20201223_2205'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FavoriteRecipes',
        ),
    ]