# Generated by Django 4.2.7 on 2023-11-29 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_login_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
    ]
