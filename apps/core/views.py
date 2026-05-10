from django.shortcuts import render
from .models import Profile

def home(request):
    profile = Profile.objects.get(active=True)
    context={
        'profile':profile
    }
    return render(request, 'core/home.html', context)
