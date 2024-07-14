from django.db import models

# Create your models here.

class Client (models.Model):
    id = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=20, null=False)
    lname = models.CharField(max_length=15, null=False)
    bday = models.DateField(null=False)

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




class Artist(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, null=False)


class Album(models.Model):
    id = models.IntegerField(primary_key=True)
    name= models.CharField(max_length=20)
    artist = models.ForeignKey(Artist, to_field="id", on_delete=models.CASCADE)


class Song(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    artist = models.ForeignKey(Artist, to_field="id", on_delete=models.CASCADE, null=False)
    song = models.ForeignKey(Album, to_field="id", on_delete=models.RESTRICT, null=True)


