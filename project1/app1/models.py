from django.db import models

# Create your models here.

class Client (models.Model):
    id = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=20, null=False)
    lname = models.CharField(max_length=15, null=False)
    bday = models.DateField(null=False)

class Post (models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    pday = models.DateField(null=False)

class ClientPost (models.Model):
    c_id = models.ForeignKey(Client, to_field="id", on_delete=models.CASCADE)
    p_id = models.ForeignKey(Post, to_field="id", on_delete=models.CASCADE)

    class Meta:
        unique_together = (("c_id", "p_id"),)
