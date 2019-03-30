from django.shortcuts import render
from .models import Job

# Create your views here.
def home(request):
    jobs = Job.objects
    return render(request, 'jobs/ngentot.html', {'jobs': jobs}) 

def cantik(request): 
    return render(request, 'template_/index.html')