# Generated by Django 4.1.2 on 2022-10-27 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_customuser_activities_log'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
