# Generated by Django 2.1.7 on 2019-12-20 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_remove_users_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExpectationsFeedbacks',
        ),
    ]