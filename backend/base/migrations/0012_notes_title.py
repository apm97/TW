# Generated by Django 4.0.3 on 2022-04-11 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_remove_notes_title_notes_name_notes_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='notes',
            name='title',
            field=models.CharField(blank=True, default=0, max_length=60, null=True),
        ),
    ]
