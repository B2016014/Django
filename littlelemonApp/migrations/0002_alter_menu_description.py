# Generated by Django 4.2.2 on 2023-06-28 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('littlelemonApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.CharField(max_length=2000),
        ),
    ]
