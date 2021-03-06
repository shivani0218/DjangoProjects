# Generated by Django 4.0.4 on 2022-05-18 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Invoice', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100)),
                ('description', models.TimeField(blank=True, default='')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('qty', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField(blank=True, default='')),
                ('total', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
