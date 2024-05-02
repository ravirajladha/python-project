from django.shortcuts import render

def home(request):
    # Make sure this path is correct
    return render(request, 'mainapp/home.html')
