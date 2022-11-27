# Generated by Django 4.1.3 on 2022-11-27 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ereader', '0011_author_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject_Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book', models.ManyToManyField(to='ereader.book')),
                ('subject', models.ManyToManyField(to='ereader.subject')),
            ],
        ),
    ]
