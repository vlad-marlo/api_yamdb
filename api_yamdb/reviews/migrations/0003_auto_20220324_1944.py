# Generated by Django 2.2.16 on 2022-03-24 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220324_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('user', '0'), ('moderator', '1'), ('admin', '2')], default=('user', '0'), max_length=10, verbose_name='role'),
        ),
    ]
