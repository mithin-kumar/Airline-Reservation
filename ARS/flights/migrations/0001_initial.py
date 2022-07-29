# Generated by Django 4.0.4 on 2022-07-26 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='flights',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('origin', models.CharField(max_length=64)),
                ('duration', models.IntegerField()),
                ('destination', models.CharField(max_length=64)),
            ],
        ),
    ]