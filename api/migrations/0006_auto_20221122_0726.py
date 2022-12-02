# Generated by Django 3.1.4 on 2022-11-22 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_author_blogs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='blogs',
        ),
        migrations.AddField(
            model_name='author',
            name='blogs',
            field=models.ManyToManyField(to='api.Blog'),
        ),
    ]
