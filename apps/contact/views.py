from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

from apps.contact.forms import ContactForm
from apps.contact.services import send_contact_notification

from apps.core.models import Person

class ContactView(FormView):
    template_name = 'contact/contact.html'

    form_class = ContactForm

    success_url = reverse_lazy('contact:contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        person = Person.objects.filter(is_me=True).first()
        context['contact'] = {
            'linkedin_url': person.linkedin_url,
            'phone_number': person.phone_number,
        }
        
        return context

    def form_valid(self, form):
        contact_message = form.save()

        try: 
            send_contact_notification(contact_message)
            messages.success(
                self.request,
                'Your message has been sent successfully.'
            )

        except Exception:
            messages.warning(
                self.request,
                (
                    'Your message was saved, but the email'
                    'notification could not be delivered.'
                )
            )        

        return super().form_valid(form)
    
    