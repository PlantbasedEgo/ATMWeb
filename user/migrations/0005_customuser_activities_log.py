# Generated by Django 4.0.6 on 2022-10-17 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_customuser_user_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='activities_log',
            field=models.JSONField(default=list, null=True),
        ),
    ]