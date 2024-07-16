from django.db import models
from datetime import datetime
# Create your models here.

class Client (models.Model):
    id = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=20, null=False)
    lname = models.CharField(max_length=15, null=False)
    bday = models.DateField(null=False)
    iday = models.DateField(null=False, default=datetime.now)
    size = models.ForeignKey("ClientSize", to_field="idsize", on_delete=models.PROTECT, null=True)


    class Meta:
        indexes = [
            models.Index(name="i_Client_id", fields=['id']),
            models.Index(name="i_Client_fname", fields=['fname']),
            models.Index(name="i_Client_lname", fields=['lname']),
        ]


class Post (models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, null=False)
    pday = models.DateField(null=False)

    class Meta:
        indexes = [
            models.Index(name="i_Post_id", fields=["id"]),
            models.Index(name="i_Post_name", fields=["name"]),
        ]

class ClientPost (models.Model):
    c_id = models.ForeignKey(Client, to_field="id", on_delete=models.CASCADE)
    p_id = models.ForeignKey(Post, to_field="id", on_delete=models.CASCADE)

    class Meta:
        unique_together = (("c_id", "p_id"),)
        indexes = [
            models.Index(name="i_ClientPost_FoerignKeys", fields=["c_id", "p_id"]),
        ]

class ClientSize (models.Model):
    CHOICES_ID = {
        'A':"xxs",
        'B':'xs',
        'C':'s',
        'D':'m',
        'E':'l',
        'F':'xl',
        'G':'xxl',
    }

    CHOICES_SIZE = {
        'XXS':'xxs',
        'XS':'xs',
        'S':'s',
        'M':'m',
        'L':'l',
        'XL':'xl',
        'XXL':'xxl',
    }

    id = models.IntegerField(primary_key=True)
    idsize = models.CharField(max_length=1, choices=CHOICES_ID, unique=True)
    size = models.CharField(max_length=3, choices=CHOICES_SIZE)
