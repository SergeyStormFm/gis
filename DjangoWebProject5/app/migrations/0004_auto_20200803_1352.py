# Generated by Django 3.0.8 on 2020-08-03 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200803_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link_npa',
            name='name',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='link_npa',
            name='to_Link_id_npa',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
