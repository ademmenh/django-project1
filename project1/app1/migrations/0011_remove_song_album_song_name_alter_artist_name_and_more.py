# Generated by Django 5.0.6 on 2024-07-14 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_alter_song_artist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='album',
        ),
        migrations.AddField(
            model_name='song',
            name='name',
            field=models.CharField(default='error', max_length=20),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='song',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='Album',
        ),
    ]
