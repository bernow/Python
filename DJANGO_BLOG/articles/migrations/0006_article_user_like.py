# Generated by Django 2.2.6 on 2019-11-18 11:11

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('articles', '0005_auto_20191118_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='user_like',
            field=models.ManyToManyField(blank=True, related_name='like_articles', to=settings.AUTH_USER_MODEL),
        ),
    ]
