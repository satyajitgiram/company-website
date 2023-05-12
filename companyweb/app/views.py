from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,"index.html")


def AboutUs(request):
    return render(request,"about.html")

def ContactUs(request):
    return render(request,"contact.html")


def Services(request):
    return render(request,"services.html")


def Team(request):
    return render(request,"team.html")


def FAQs(request):
    return render(request,"faqs.html")
