# Generated by Django 5.0.3 on 2024-04-04 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voting_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='created_by',
        ),
        migrations.DeleteModel(
            name='Option',
        ),
        migrations.DeleteModel(
            name='Poll',
        ),
    ]