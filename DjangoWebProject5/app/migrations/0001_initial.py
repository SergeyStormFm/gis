# Generated by Django 3.0.8 on 2020-08-03 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Years',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=4)),
                ('is_active', models.IntegerField(blank=True, choices=[(1, 'активно'), (0, 'Не активно')], default=1, help_text='1->активно, 0->Не активно', null=True)),
            ],
            options={
                'verbose_name': 'Год',
                'verbose_name_plural': 'Года',
            },
        ),
        migrations.CreateModel(
            name='npa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vid_del', models.IntegerField(blank=True, choices=[(1, 'ОД'), (0, 'АХД')], default=1, help_text='1->ОД, 0->АХД', null=True, verbose_name='Вид деятельности')),
                ('vid', models.IntegerField(blank=True, choices=[(1, 'Приказы'), (0, 'Распоряжение')], default=1, help_text='1->Приказы, 0->Распоряжение', null=True, verbose_name='Вид')),
                ('nomer', models.CharField(max_length=10, verbose_name='Номер')),
                ('date', models.DateTimeField(verbose_name='Дата')),
                ('name', models.CharField(max_length=1000, verbose_name='Наименовение')),
                ('status', models.IntegerField(blank=True, choices=[(1, 'Действующий'), (0, 'Утратил силу')], default=1, help_text='1->Действующий, 0->Утратил силу', null=True, verbose_name='Статус')),
                ('kol_list', models.IntegerField(blank=True, default=1, null=True, verbose_name='Количество страниц документа')),
                ('kol_prl', models.IntegerField(blank=True, default=1, null=True, verbose_name='Количество страниц приложения')),
                ('razrab', models.CharField(max_length=50, verbose_name='Разработчик')),
                ('document', models.FileField(upload_to='./%Y/%m/%d/', verbose_name='Документ')),
                ('is_active', models.IntegerField(blank=True, choices=[(1, 'активно'), (0, 'Не активно')], default=1, help_text='1->активно, 0->Не активно', null=True, verbose_name='----------')),
                ('year', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Years')),
            ],
            options={
                'verbose_name': 'НПА',
                'verbose_name_plural': 'НПА',
            },
        ),
        migrations.CreateModel(
            name='link_npa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to_Link_id_npa', models.IntegerField()),
                ('id_npa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.npa')),
            ],
            options={
                'verbose_name': 'link',
                'verbose_name_plural': 'link',
            },
        ),
    ]
