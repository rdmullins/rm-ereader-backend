# Generated by Django 4.1.3 on 2022-11-27 14:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ereader', '0007_book_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farthest_read', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ereader.book')),
                ('book_status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ereader.book_status')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
