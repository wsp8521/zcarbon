from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import logout


#renders the login page
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_admin')  # redirect for system home page
        else:
            return render(request, 'login.html', {'error': 'Credenciais inválidas'})

    return render(request, 'login.html')



#'logout' view
def logout_view(request):
    logout(request)
    return redirect('home')  # back to the home page