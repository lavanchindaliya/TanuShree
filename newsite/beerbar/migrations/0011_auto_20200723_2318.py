# Generated by Django 3.0.5 on 2020-07-23 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beerbar', '0010_auto_20200723_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gin',
            name='category',
            field=models.CharField(default='gin', max_length=50),
        ),
    ]
