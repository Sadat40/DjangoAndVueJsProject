# Generated by Django 5.0.4 on 2024-04-18 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='numberOfCharacters',
        ),
    ]