# Generated by Django 3.1.14 on 2022-03-29 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cities', '0002_auto_20220324_1817'),
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Номер поезда')),
                ('travel_time', models.PositiveSmallIntegerField(verbose_name='Время в пути')),
                ('from_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_city_set', to='cities.city', verbose_name='Откуда')),
                ('to_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_city_set', to='cities.city', verbose_name='Куда')),
            ],
            options={
                'verbose_name': 'Поезд',
                'verbose_name_plural': 'Поезда',
                'ordering': ['name'],
            },
        ),
    ]
