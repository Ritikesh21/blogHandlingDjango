# Generated by Django 3.1.4 on 2022-11-15 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0002_auto_20221115_1243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='phone',
            new_name='number',
        ),
    ]