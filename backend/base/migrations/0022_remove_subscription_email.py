# Generated by Django 4.0.3 on 2022-06-13 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0021_alter_subscription_email_alter_subscription_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='email',
        ),
    ]