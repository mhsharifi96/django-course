# Generated by Django 4.1.3 on 2022-11-03 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='sample_number',
            field=models.IntegerField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
