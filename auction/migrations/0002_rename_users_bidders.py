# Generated by Django 4.0.6 on 2022-07-15 17:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='users',
            new_name='bidders',
        ),
    ]
