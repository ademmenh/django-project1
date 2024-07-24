from django.shortcuts import render, HttpResponse
from . import forms
from . import models






def form(request):

    if request.method == "GET":
        form = forms.FormUser()
        context = {"form":form, }
        return render(request, 'form.html', context)


    elif request.method == "POST":
        form = forms.FormUser(request.POST)

        if form.is_valid():
            formSubmition = request.POST
            form.IsCorrect(formSubmition['fname'])

            models.Users.objects.create(fname=formSubmition['fname'])

            context = {'fname':request.POST['fname'], }
            return render(request, 'done.html', context)

    else:
        context = {}
        render(request, 'error.html', context)






def home(request):
    return HttpResponse("this is home.")

