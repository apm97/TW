# Generated by Django 4.0.3 on 2022-06-12 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
