# Generated by Django 4.1.3 on 2022-11-24 19:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0002_myuser_temp_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myuser',
            old_name='temp_password',
            new_name='token',
        ),
    ]