# Generated by Django 4.1.3 on 2022-11-03 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('profile_picture', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('subtitle', models.CharField(max_length=20)),
                ('slug', models.SlugField()),
                ('thumbnail', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('overview', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='')),
                ('featured', models.BooleanField()),
                ('status', models.CharField(choices=[('en', 'enable'), ('de', 'disable'), ('da', 'draft')], max_length=2)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.author')),
                ('categories', models.ManyToManyField(to='blog.category')),
            ],
        ),
    ]
