from django import forms

class InputForm(forms.Form):

    CHOICES_GENDER = {
    "m":"man",
    "w":"woman",
    }

    fname = forms.CharField(max_length=20)
    lname = forms.CharField(max_length=20)
    gender = forms.ChoiceField(choices=CHOICES_GENDER)
    time = forms.TimeField()
