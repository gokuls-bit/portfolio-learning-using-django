from django.shortcuts import render

def home(request):
    return render(request, 'portfolio/home.html')

def education(request):
    return render(request, 'portfolio/education.html')

def projects(request):
    return render(request, 'portfolio/projects.html')

def experience(request):
    return render(request, 'portfolio/experience.html')

def contact(request):
    return render(request, 'portfolio/contact.html')
