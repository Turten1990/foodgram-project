# Generated by Django 3.1.4 on 2021-01-28 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0024_recipetagmapping'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipetagmapping',
            old_name='tag',
            new_name='tags',
        ),
        migrations.AlterField(
            model_name='recipetagmapping',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipetags', to='recipes.recipe'),
        ),
    ]
