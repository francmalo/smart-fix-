# Generated by Django 4.0 on 2022-01-03 12:39

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fullName', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phoneNumber', models.CharField(max_length=20, unique=True)),
                ('role', models.CharField(max_length=30)),
                ('businessName', models.CharField(blank=True, max_length=200, null=True)),
                ('businessDescription', models.TextField(blank=True, null=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('businessCategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.businesscategory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
