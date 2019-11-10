# Generated by Django 2.2.3 on 2019-11-10 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_url', models.CharField(max_length=75)),
                ('long_url', models.CharField(max_length=100)),
                ('date_encoded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
