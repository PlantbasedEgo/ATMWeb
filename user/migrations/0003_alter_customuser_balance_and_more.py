# Generated by Django 4.0.6 on 2022-09-04 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_customuser_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='balance',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=12, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='withdrawal_fee',
            field=models.DecimalField(decimal_places=4, default=1.0005, max_digits=6, null=True),
        ),
    ]
