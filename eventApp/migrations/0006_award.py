# Generated by Django 4.2.7 on 2023-11-27 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventApp', '0005_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Award',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('desc', models.TextField()),
                ('title_1', models.CharField(max_length=255)),
                ('desc_1', models.TextField()),
                ('title_2', models.CharField(max_length=255)),
                ('desc_2', models.TextField()),
                ('title_3', models.CharField(max_length=255)),
                ('desc_3', models.TextField()),
            ],
        ),
    ]
