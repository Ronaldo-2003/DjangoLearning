from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello user , you are at chai aur Django home page.")
    return render(request , 'website/index.html')

def contact(request):
    return render(request , 'website/contact.html')

def about(request):
    return render(request , 'website/about.html')
