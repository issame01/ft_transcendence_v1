# Generated by Django 5.1.3 on 2024-12-01 04:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0034_playerstats_rename_fit_u1_gameresult_player1_fit_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='blocked_friends',
            field=models.ManyToManyField(blank=True, related_name='blocked_friends', to=settings.AUTH_USER_MODEL),
        ),
    ]
