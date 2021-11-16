from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def abaut(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def partfolio(request):
    return render(request, 'portfolio.html')

def pricing(request):
    return render(request, 'pricing.html')

def contact(request):
    return render(request, 'contact.html')