# Generated by Django 2.2.5 on 2019-09-24 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='letter',
            name='image',
            field=models.ImageField(upload_to='letter/'),
        ),
        migrations.AlterField(
            model_name='word',
            name='image',
            field=models.ImageField(upload_to='word/'),
        ),
    ]
