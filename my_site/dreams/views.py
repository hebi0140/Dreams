from django.shortcuts import render
from .models import Dreams

# Create your views here.

def index(request):
    return render(request, 'dreams/index.html')

def about(request):
    musician = Dreams.objects.all()
    context = {'musician': musician}
    return render(request, 'dreams/about.html', context)

def contact(request):
    return render(request, 'dreams/contact.html')
