# Generated by Django 5.0.7 on 2024-07-19 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_alter_userprofile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='image',
            new_name='profile_image',
        ),
    ]
