# Generated by Django 3.1.4 on 2022-11-15 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0005_auto_20221115_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
