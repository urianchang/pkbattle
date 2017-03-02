from django.shortcuts import render, redirect

# Create your views here.
def start(request):
    return render(request, 'logreg/start.html')

def prof(request):
    return render(request, 'logreg/login.html')

def login(request):
    print "**LOGIN**"
    return redirect('/prof')

def register(request):
    print "**REG**"
    return redirect('/prof')
