# Generated by Django 4.1.7 on 2023-03-27 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_businessname_account_county_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('client', 'client'), ('technician', 'technician')], max_length=30),
        ),
    ]
