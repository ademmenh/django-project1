# Generated by Django 5.0.6 on 2024-07-15 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0020_client_size_alter_clientsize_idsize'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='size',
        ),
        migrations.DeleteModel(
            name='ClientSize',
        ),
    ]
