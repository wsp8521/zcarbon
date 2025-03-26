from django.shortcuts import render

#renders the home page
def home(request):
    #lógica da view aqui
    
    return render(request, 'index.html')


#renders the diagnostics page
def diagnostics(request):
    #lógica da view aqui
    
    return render(request, 'diagnostics_form.html')