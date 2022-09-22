# Generated by Django 4.1 on 2022-09-22 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WatchListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('watched', models.BooleanField(default=True)),
                ('title', models.TextField(default='')),
                ('rating', models.FloatField(default=0)),
                ('release_date', models.DateField()),
                ('review', models.TextField(default='')),
            ],
        ),
    ]
