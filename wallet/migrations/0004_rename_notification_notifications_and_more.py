# Generated by Django 4.0.6 on 2022-08-01 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0003_rename_notifications_notification_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Notification',
            new_name='Notifications',
        ),
        migrations.RenameModel(
            old_name='Receipt',
            new_name='Receipts',
        ),
    ]