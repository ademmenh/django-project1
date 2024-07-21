from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError





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

    def __str__(self):
        return f"{self.id}, {self.fname}, {self.lname}, {self.salary}"




class ClientSalary(models.Model):

    CHOICES_RATING={
        'A':'A',
        'B':'B',
        'C':'C',
        'D':'D',
        'E':'E',
        'F':'F',
    }

    salary = models.IntegerField(primary_key=True)
    rating = models.CharField(max_length=1, choices=CHOICES_RATING, null=False)


class Users (models.Model):
    id = models.BigAutoField(primary_key=True)
    fname = models.CharField(max_length=20, null=False)

    def __str__(self):
        return str(self.id) + ' ' + str(self.fname)
