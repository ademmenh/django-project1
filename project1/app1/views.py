from django.shortcuts import render, HttpResponse
from . import forms
from . import models






def form(request):
    if request.method == "GET":
        form = forms.FormUser()

    elif request.method == "POST":
        form = forms.FormUser(request.POST)

        if form.is_valid():
            formSubmition = request.POST
            form.fnameIsCorrect(formSubmition['fname'])

            models.User.objects.create(fname=formSubmition['fname'])
            return HttpResponse("done!")
    
    context = {"form":form, }
    return render(request, 'form.html', context)





def home(request):
    return HttpResponse("this is home.")

