# Generated by Django 4.1.3 on 2022-12-02 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ereader', '0019_alter_bookmetadata_cover_alter_bookmetadata_epub'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmetadata',
            name='cover',
        ),
        migrations.RemoveField(
            model_name='bookmetadata',
            name='epub',
        ),
    ]