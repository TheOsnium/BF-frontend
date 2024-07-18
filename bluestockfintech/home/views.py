from django.shortcuts import render, redirect

def home(request):
    # print("Heywe are in home")
    return render(request, 'index12.html')

def dashboard(request):
    return render(request, 'admindash.html')

def adminlogin(request):
    return render(request, 'adminlogin.html')

def adminforgetpass(request):
    return render(request, 'adminforgetpass.html')

def adminsignup(request):
    return render(request, 'adminsignup.html')

def upcomingIPO(request):
    return render(request, 'upcomingIPO.html')

def registerIPO(request):
    return render(request, 'registerIPO.html')