from django.shortcuts import render, HttpResponse
from . import forms

# Create your views here.

def form(request):
    form = forms.InputForm()
    context = {"form": form}

    return render(request, "form.html", context)

def home(request):
    return HttpResponse("this is home.")