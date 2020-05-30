# Generated by Django 2.1.7 on 2019-12-20 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20191220_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='profile'),
        ),
        migrations.AlterField(
            model_name='expectationsfeedbacks',
            name='exp_timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='expectationsfeedbacks',
            name='feedback_timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
