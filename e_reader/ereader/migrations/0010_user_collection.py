# Generated by Django 4.1.3 on 2022-11-27 15:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ereader', '0009_collection'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collection', models.ManyToManyField(to='ereader.collection')),
                ('user', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
