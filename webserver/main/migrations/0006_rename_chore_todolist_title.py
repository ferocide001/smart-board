# Generated by Django 4.0.3 on 2022-03-24 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_todolist_complete_todolist_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todolist',
            old_name='chore',
            new_name='title',
        ),
    ]