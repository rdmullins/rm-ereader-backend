# Generated by Django 4.1.3 on 2022-11-27 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ereader', '0004_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gutenberg_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=255)),
            ],
        ),
    ]