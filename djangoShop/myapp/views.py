from django.shortcuts import render, redirect
from .models import Tour
from django.http import HttpResponse
from .form import ContactForm

# Create your views here.

# def index(request):
#     return HttpResponse("Asia shop")

def index(request):
    tours = Tour.objects.all()
    context = {'tours':tours}
    return render(request, 'tours/index.html', context)

def home_view(request):
    return render(request, 'myapp/home.html')

def contact_view(request):
    if request.method =="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect('contact-success')
    else:
        form = ContactForm()
    context = {'form':form}
    return render(request, 'myapp/contact.html', context)

def contact_success_view(request):
    return render(request, 'myapp/contact_success.html')