# Generated by Django 3.2.12 on 2022-05-30 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messager', '0002_thread_updated'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='thread',
            options={'ordering': ['-updated']},
        ),
    ]
