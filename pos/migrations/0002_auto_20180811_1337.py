# Generated by Django 2.1 on 2018-08-11 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Order_Item',
            new_name='OrderItem',
        ),
    ]
