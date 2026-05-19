from django.shortcuts import render
from .models import Profile

def home(request):
    profile = Profile.objects.get(active=True)
    context={
        'profile':profile
    }
    return render(request, 'core/home.html', context)

def about_view(request):
    profile = Profile.objects.get(active=True)
    focus_expertise_groups = profile.focus_expertise_groups.all().order_by('order')
    focus_areas = profile.abouts.all().filter(order__lt=5) or False
    open_to = profile.abouts.filter(order=5).first() or False
    context = {
        'profile': profile,
        'focus_expertise_groups': focus_expertise_groups,
        'focus_areas': focus_areas,
        'open_to': open_to
    }

    return render(request, 'core/about.html', context)
