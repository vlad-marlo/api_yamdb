# Generated by Django 3.0 on 2022-03-22 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220321_1756'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'ordering': ('id',)},
        ),
    ]
