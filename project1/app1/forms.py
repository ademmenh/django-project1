from django import forms
from . import models
from django.core.exceptions import ValidationError








class FormClient(forms.Form):
    fname = forms.CharField(max_length=20, label="first name:", required=True, error_messages={'required':'you have to enter your first name !!!'}, )

    






class FormUsers(forms.Form):
    fname = forms.CharField(max_length=20, label='First Name:', required=True, error_messages={'required':"you have to enter your first name."}, )
    lname = forms.CharField(max_length=20, label='Last Name:', required=True, error_messages={'required':"you have to enter you last name."}, )
    age = forms.IntegerField(label='Age', required=True, error_messages={'requied':"you have to enter you age."}, )



    def IsCorrect(self, dic):

        if dic.get('fname')[0].islower():
            raise ValidationError('the first letter in first name is in lowerCase.')
        
        if dic.get('lname')[0].islower():
            raise ValidationError('the first letter in last name is in lowerCase.')
            
        if int(dic.get('age'))<0 or int(dic.get('age'))>100:
            raise ValidationError('You age is weird!!')
            
        return True
    