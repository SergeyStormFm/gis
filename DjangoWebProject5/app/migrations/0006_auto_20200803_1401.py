# Generated by Django 3.0.8 on 2020-08-03 11:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20200803_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='link_npa',
            old_name='id_nda',
            new_name='id_npa',
        ),
    ]
