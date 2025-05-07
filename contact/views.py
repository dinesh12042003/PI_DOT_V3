from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, 'contact.html')

def cookie_policy(request):
    return render(request, 'cookie_policy.html')

def terms_coditions(request):
    return render(request, 'terms_coditions.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')