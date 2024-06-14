from django.shortcuts import render 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to home after login
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('home')  # Redirect to home after logout


  

def home(request): 

    return render(request, "home.html") 

  

def projects(request): 

    return render(request, "projects.html") 

  

def contact(request): 

    return render(request, "contact.html")
