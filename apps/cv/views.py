from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.utils.text import slugify

from apps.cv.selectors import  get_cv_context
from apps.cv.services.pdf_client import generate_cv_pdf

from decouple import config

def cv_print_view(request):
    context = get_cv_context()

    return render(
        request,
        'cv/cv_print.html',
        context,
    )

def cv_download_view(request):
    
    context = get_cv_context() 
    person = context.get('person', None)
    profile = context.get('profile', None)

    print_url = f'{config('BASE_URL', default='http://127.0.0.1:8000')}{reverse('cv_print')}'

    pdf = generate_cv_pdf(print_url)
    if profile.cv_slug :
        filename = f"{profile.cv_slug}.pdf"
    else:
        filename = f'{slugify(person.name)}_cv.pdf'

    response = HttpResponse(
        pdf, content_type='application/pdf'
    )

    response['Content-Disposition'] = (f'attachment; filename={filename}')

    return response 