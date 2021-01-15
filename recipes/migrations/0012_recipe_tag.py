# Generated by Django 3.1.4 on 2020-12-21 14:35

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0011_auto_20201214_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='tag',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Завтрак', 'Завтрак'), ('Обед', 'Обед'), ('Ужин', 'Ужин')], default='Обед', max_length=50),
        ),
    ]
