
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

#renders the home system page
@login_required
def home_admin(request):
    #lógica da view aqui
    if request.user.is_staff:
        return render(request, 'home_admin.html')
    else:
        return redirect('home_user')


#renders the home system page
@login_required
def Desh(request):
    #lógica da view aqui
    
    return render(request, 'page_name.html')


#renders the home system page
@login_required
def report(request):
    #lógica da view aqui
    
    return render(request, 'page_name.html')


#renders the home system page
@login_required
def user(request):
    #lógica da view aqui
    
    return render(request, 'page_name.html')