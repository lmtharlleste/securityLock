# Generated by Django 4.1.4 on 2024-02-12 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='personal_cod',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]