from django.shortcuts import render, HttpResponse
from . import forms
from . import models

# Create your views here.

def form(request):
    if (request.method == "POST"):
        form = forms.FormUser(request.POST)


        if form.is_valid():
            vfname = request.POST['fname']
            form.fnameIsCorrect(vfname)


            ouser1 = models.User.objects.create(fname="{vfname}")
            return HttpResponse("done!")
    else:
        form = forms.FormUser()
    
    #form = forms.FormUser()
    context = {"form": form}
    return render(request, 'form.html', context)





def home(request):
    return HttpResponse("this is home.")

