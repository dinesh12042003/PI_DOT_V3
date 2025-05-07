from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'PiDot\About.html')

def careers(request):
    return render(request, 'PiDot\Careers.html')

def careers_register(request):
    return render(request, 'PiDot\Careers_register.html')

def leadership(request):
    return render(request, 'PiDot\leadership.html')

def newsroom(request):
    return render(request, 'PiDot/Newsroom.html')