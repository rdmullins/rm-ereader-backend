# Generated by Django 4.1.3 on 2022-11-27 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ereader', '0006_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255)),
            ],
        ),
    ]