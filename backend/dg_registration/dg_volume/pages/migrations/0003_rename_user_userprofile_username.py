# Generated by Django 5.0.7 on 2024-07-19 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_alter_note_content_alter_note_title_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='user',
            new_name='username',
        ),
    ]
