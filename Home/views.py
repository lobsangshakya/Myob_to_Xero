from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

# Homepage view
def index(request):
    return render(request, 'index.html')

# login page 
def login_page(request):
    return render(request, 'login.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user) 
            return redirect('main')  
        else:
            messages.error(request, "Invalid credentials")
            return render(request, 'main.html', {'error': 'Invalid credentials'})
    return render(request, 'main.html')


# Main Page
def main(request):
    return render(request, 'main.html')

# Signup view (if you have one, not shown in the code)
def signup(request):
    return render(request, 'signup.html')
