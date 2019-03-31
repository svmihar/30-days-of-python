from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def signup(request):
    if request.method == 'POST': 
        #the user wants to sign up. 
        if request.POST['password'] == request.POST['confirmation']: 
            try:
                User.objects.get(username = request.POST['username'])
                return render(request, 'signup.html', {'error': 'username is taken'})
            except User.DoesNotExist: 
                user = User.objects.create_user(request.POST['username'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')

    else: 
        pass
        # user want to login 
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')


def logout(request):
    # TODO: route to home page.  
    return render(request, 'signup.html')