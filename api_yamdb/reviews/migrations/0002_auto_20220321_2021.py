# Generated by Django 3.0 on 2022-03-21 17:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-slug']},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'ordering': ['-slug']},
        ),
        migrations.AlterModelOptions(
            name='title',
            options={'ordering': ['-name']},
        ),
    ]
