# Generated by Django 2.2 on 2019-04-07 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahck', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packet',
            name='description_in_json',
            field=models.TextField(default='{}', verbose_name='json packet description'),
        ),
    ]
