# Generated by Django 3.2.16 on 2023-03-19 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='sub_total',
            field=models.IntegerField(null=True),
        ),
    ]