# Generated by Django 4.0.3 on 2022-04-11 22:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_notes_createdat_alter_notes_content'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserMember',
        ),
    ]