# Generated by Django 3.2.16 on 2023-03-19 14:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0004_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(default=-1.0, on_delete=django.db.models.deletion.CASCADE, to='user.role'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='user',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='role',
            name='display_name',
            field=models.CharField(default='', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='role',
            name='name',
            field=models.CharField(default='', max_length=30, null=True),
        ),
    ]