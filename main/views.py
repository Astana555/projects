from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/feedback.html')

def about(request):
    return HttpResponse("<h4>Страница про нас</h4>")






#на пересмотр мне

'''
# Create your views here.

# pets/views.py
from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = FeedbackForm()

    return render(request, 'feedback.html', {'form': form})
'''

