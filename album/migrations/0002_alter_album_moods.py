# Generated by Django 5.0.7 on 2024-07-19 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0001_initial'),
        ('mood', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='moods',
            field=models.ManyToManyField(blank=True, related_name='albums', to='mood.mood'),
        ),
    ]
