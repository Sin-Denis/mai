# Generated by Django 2.2 on 2019-04-07 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ahck', '0004_auto_20190407_1022'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actofshortage',
            old_name='descriprion_in_json',
            new_name='description_in_json',
        ),
    ]