# Generated by Django 4.0.6 on 2022-07-15 17:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_rename_users_bidders'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='bids',
            new_name='bid',
        ),
        migrations.RenameModel(
            old_name='bidders',
            new_name='user',
        ),
    ]
