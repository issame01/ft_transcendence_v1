# Generated by Django 5.1 on 2024-08-12 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0025_userprofile_deleted_at_userprofile_is_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
            ],
        ),
    ]
