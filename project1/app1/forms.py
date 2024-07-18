from django import forms
from . import models

class FormClient(forms.ModelForm):
    class Meta:
        model = models.Client
        fields = ["fname", "lname", "bday", ]

