from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import FeedbackForm

def index(request):
    return render(request, 'main/feedback.html')

def about(request):
    return HttpResponse("<h4>Страница про нас</h4>")

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
        else:
            form = FeedbackForm()
        return render(request, 'feedback.html', {'form': form})

def error_page(request):
    return render(request, 'error.html')


# Create your views here.
def feedback(request):
    cats = Pet.objects.filter(type='cat')
    dogs = Pet.objects.filter(type='dog')
    return render(request, 'feedback.html', {'cats': cats, 'dogs': dogs})

