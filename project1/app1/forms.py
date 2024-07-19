from django import forms
from . import models

from django.core.exceptions import ValidationError

class FormClient(forms.Form):
    fname = forms.CharField(max_length=20, label="First Name:", required=True, initial="enter your name here..." )

    
    
class FormUser(forms.Form):
    fname = forms.CharField(max_length=20, label="First Name:", required=True, error_messages={"required":"you have to enter your name."})

    def fnameIsCorrect(self, object):
        if object[0].islower():
            raise ValidationError("the first letter is in LowerCase.")
            
        return object