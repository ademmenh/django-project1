# Generated by Django 5.0.6 on 2024-07-14 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0011_remove_song_album_song_name_alter_artist_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
