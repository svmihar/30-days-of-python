from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


# Create your views here.
def signup(request):
    if request.method == 'POST': 
        #the user wants to sign up. 
        if request.POST['password'] == request.POST['confirmation']: 
            try:
                user = User.objects.get(username = request.POST['username'])
                return render(request, 'signup.html', {'error': 'username is taken'})
            except User.DoesNotExist: 
                user = User.objects.create_user(request.POST['username'], password=request.POST['confirmation'])
                auth.login(request, user)
                return redirect('home')
        else: 
            return render(request, 'signup.html', {'error': 'password must match'})
    else: 
        pass
        # user want to login 
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None: 
            auth.login(request, user)
            return redirect('home')
        else: 
            return render(request, 'login.html', {'error':'username or password is invalid'})
    else: 
        return render(request, 'login.html')


def logout(request):
    if request.method== 'POST': 
        auth.logout(request)
        return redirect('home')