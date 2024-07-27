from django.shortcuts import render, HttpResponse
from . import forms
from . import models

from django.views import generic

from django.core.exceptions import ValidationError





def form(request):

    if request.method == "GET":
        form = forms.FormUsers()
        # print(form)
        context = {'form': form, }
        return render(request, 'form.html', context)

    elif request.method == "POST":
        form = forms.FormUsers(request.POST)
        # print(form)

        if form.is_valid():
            Submitionform = request.POST
            form.IsCorrect(Submitionform)

            models.Users.objects.create(fname=Submitionform['fname'], lname=Submitionform['lname'], age=Submitionform['age'])

            context = {'fname':request.POST['fname'], }
            return render(request, 'done.html', context)
        else:
            return render(request, 'error.html', {})
                
    else:
        context = {}
        render(request, 'error.html', context)






def home(request):
    return HttpResponse("this is home.")