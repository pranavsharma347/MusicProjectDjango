# Generated by Django 3.2.5 on 2021-07-16 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0004_comment_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]