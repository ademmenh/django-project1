from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError


# Create your models here.

class Client (models.Model):
    id = models.IntegerField(primary_key=True)
    fname = models.CharField(max_length=20, null=False)
    lname = models.CharField(max_length=15, null=False)
    bday = models.DateField(null=False)
    iday = models.DateField(default=datetime.now, null=False)
    salary = models.ForeignKey("ClientSalary", to_field="salary", on_delete=models.CASCADE, null=True)

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


class ClientSalary(models.Model):
    
    CHOICES_RATING={
        'A':'',
        'B':'',
        'C':'',
        'D':'',
        'E':''
    }

    salary = models.IntegerField(primary_key=True)
    rating = models.CharField(max_length=1, choices=CHOICES_RATING, null=False)

    def objectscreate(self):
        if self.rating not in self.CHOICES_RATING:
            raise ValidationError(f"the rating {self.rating} is invalid")
        else:
            ClientSalary.objects.create(salary=self.salary, rating=self.rating)
    