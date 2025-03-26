
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

#renders the home system page
@login_required
def home_user(request):
    #lógica da view aqui
    
    return render(request, 'home_user.html')


#renders the home system page
@login_required
def inventory(request):
    #lógica da view aqui
    
    return render(request, 'home_user.html')



#renders the home system page
@login_required
def diagnostic(request):
    #lógica da view aqui
    
    return render(request, 'home_user.html')



def data_collection(request):
    #lógica da view aqui
    
    return render(request, 'home_user.html')

