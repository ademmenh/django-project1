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


class ClientSalary(models.Model):

    CHOICES_RATING={
        'A':'',
        'B':'',
        'C':'',
        'D':'',
        'E':'',
        'F':'',
    }

    salary = models.IntegerField(primary_key=True)
    rating = models.CharField(max_length=1, choices=CHOICES_RATING, null=False)

    def objects_create(self):
        if self.rating not in self.CHOICES_RATING:
            raise ValidationError(f"the rating {self.rating} is invalid")
        else:
            ClientSalary.objects.create(salary=self.salary, rating=self.rating)

