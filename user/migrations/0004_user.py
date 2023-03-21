# Generated by Django 3.2.16 on 2023-03-19 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=50, null=True)),
                ('last_name', models.CharField(max_length=50, null=True)),
                ('user_name', models.CharField(max_length=30, unique=True)),
                ('mobile', models.CharField(max_length=10, null=True)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('password_hash', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('intro', models.TextField(max_length=100, null=True)),
                ('profile', models.TextField(max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]