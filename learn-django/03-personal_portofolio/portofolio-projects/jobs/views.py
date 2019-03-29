from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'jobs/ngentot.html') 

def cantik(request): 
    return render(request, 'template_/index.html')