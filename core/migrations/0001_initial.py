# Generated by Django 4.1.4 on 2024-02-12 00:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('username', models.CharField(blank=True, max_length=150, null=True, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('personal_cod', models.CharField(max_length=16)),
                ('otp_enabled', models.BooleanField(default=False)),
                ('otp_verified', models.BooleanField(default=False)),
                ('otp_base32', models.CharField(max_length=255, null=True)),
                ('otp_auth_url', models.CharField(max_length=255, null=True)),
                ('image_profile', models.ImageField(blank=True, null=True, upload_to='images/avatar')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, to='auth.group', verbose_name='grupos')),
                ('user_permissions', models.ManyToManyField(blank=True, to='auth.permission', verbose_name='permissões')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]