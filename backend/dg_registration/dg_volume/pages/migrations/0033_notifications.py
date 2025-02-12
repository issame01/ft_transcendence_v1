# Generated by Django 5.1.3 on 2024-11-21 04:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0032_conversation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notify_at', models.DateTimeField()),
                ('user1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1_notifications', to='pages.userprofile')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2_notifications', to='pages.userprofile')),
            ],
            options={
                'unique_together': {('user1', 'user2')},
            },
        ),
    ]
