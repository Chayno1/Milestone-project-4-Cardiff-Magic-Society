# Generated by Django 3.2 on 2022-04-10 10:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('magician', '0002_performer_display'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='performer',
            name='image_url',
        ),
    ]
