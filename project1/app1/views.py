from django.shortcuts import render, HttpResponse
from . import forms

# Create your views here.

def form(request):

    if (request.method == "POST"):
        form = forms.FormClient(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("done!")
    else:
        form = forms.FormClient()

    context = {"form": form}
    print(form)
    return render(request, 'form.html', context)


def home(request):
    return HttpResponse("this is home.")