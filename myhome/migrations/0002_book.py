# Generated by Django 2.2.24 on 2021-10-10 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myhome', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=50)),
                ('publish', models.CharField(max_length=100)),
                ('abstract', models.TextField()),
                ('img_url', models.CharField(max_length=150)),
                ('pub_data', models.DateField()),
                ('priice', models.FloatField()),
            ],
        ),
    ]
