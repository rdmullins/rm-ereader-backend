# Generated by Django 4.1.3 on 2022-11-27 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ereader', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('dob', models.DateField(blank=True)),
                ('dod', models.DateField(blank=True)),
            ],
        ),
    ]
