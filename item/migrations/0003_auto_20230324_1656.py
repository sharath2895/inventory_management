# Generated by Django 3.2.16 on 2023-03-24 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='available',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='created_by',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='defective',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='quantity',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='sold',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='item',
            name='updated_by',
            field=models.SmallIntegerField(),
        ),
    ]
