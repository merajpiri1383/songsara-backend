# Generated by Django 5.0.7 on 2024-07-17 08:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genre', '0002_alter_genre_name_alter_genre_slug'),
        ('mood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, unique=True)),
                ('slug', models.SlugField(max_length=300, unique=True)),
                ('image', models.ImageField(upload_to='playlist/images')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to='genre.genre')),
                ('moods', models.ManyToManyField(related_name='playlists', to='mood.mood')),
            ],
        ),
    ]