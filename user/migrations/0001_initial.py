# Generated by Django 4.0.6 on 2022-09-04 09:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='Username')),
                ('first_name', models.CharField(max_length=15, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=25, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email Address')),
                ('balance', models.DecimalField(decimal_places=5, default=0, max_digits=10)),
                ('withdrawal_fee', models.DecimalField(decimal_places=6, default=1.0005, max_digits=6)),
                ('user_id', models.DecimalField(decimal_places=0, default=0, max_digits=5)),
                ('about', models.TextField(blank=True, max_length=250, verbose_name='About')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date join')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
