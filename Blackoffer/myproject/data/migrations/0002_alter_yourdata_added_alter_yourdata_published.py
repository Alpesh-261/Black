# Generated by Django 4.2.8 on 2023-12-07 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yourdata',
            name='added',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='yourdata',
            name='published',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
