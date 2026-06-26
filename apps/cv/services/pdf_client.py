import requests

from django.conf import settings

PDF_SSERVICE_URL = settings.PDF_SERVICE_URL

def generate_cv_pdf(cv_url: str):
    response = requests.post(
        f'{PDF_SSERVICE_URL}/api/pdf/generate',
        json = { 'url': cv_url ,},
        timeout = 60
    )

    response.raise_for_status()

    return response.content

