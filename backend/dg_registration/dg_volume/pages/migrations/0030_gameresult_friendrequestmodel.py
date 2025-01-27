# Generated by Django 5.1.2 on 2024-10-27 00:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0029_alter_chatmessage_receiver_alter_chatmessage_sender_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winner', models.CharField(max_length=10)),
                ('user1_score', models.IntegerField()),
                ('user2_score', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('fit_u1', models.IntegerField()),
                ('fit_u2', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FriendRequestModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('accepter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='received_request', to='pages.userprofile')),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_request', to='pages.userprofile')),
            ],
        ),
    ]
