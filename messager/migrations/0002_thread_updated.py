# Generated by Django 3.2.12 on 2022-05-30 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]