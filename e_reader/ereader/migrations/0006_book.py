# Generated by Django 4.1.3 on 2022-11-27 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ereader', '0005_gutenberg_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('gut_id', models.IntegerField()),
                ('lib_id', models.IntegerField()),
                ('gut_issued', models.DateField(blank=True)),
                ('gut_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ereader.gutenberg_type')),
            ],
        ),
    ]
