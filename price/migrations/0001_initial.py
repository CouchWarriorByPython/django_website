# Generated by Django 3.2.8 on 2021-10-08 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pc_value', models.CharField(max_length=20, verbose_name='Цена')),
                ('pc_description', models.CharField(max_length=200, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Цены',
                'verbose_name_plural': 'Цена',
            },
        ),
        migrations.CreateModel(
            name='PriceTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pt_title', models.CharField(max_length=200, verbose_name='Услуга')),
                ('pt_old_price', models.CharField(max_length=200, verbose_name='Старая цена')),
                ('pt_new_price', models.CharField(max_length=200, verbose_name='Новая цена')),
            ],
            options={
                'verbose_name': 'Услугу',
                'verbose_name_plural': 'Услуги',
            },
        ),
    ]
