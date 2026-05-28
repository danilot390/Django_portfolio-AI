from django import forms

from apps.contact.models import ContactMessage

class ContactForm(forms.ModelForm):

    base_classes = (
        "w-full rounded-xl border border-gray-100 "
        "bg-white px-4 py-3 text-gray-600 "
        "placeholder:text-gray-400 "
        "focus:outline-none focus:ring-2 "
        "focus:ring-blue-500/20 focus:border-blue-500 "
        "shadow-xl transition duration-200"
    )


    class Meta:
        model = ContactMessage

        fields = [
            'name', 'email', 'subject',
            'message',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your name'
            }), 
            'email': forms.EmailInput(attrs={
                'placeholder': 'your@email.com'
            }), 
            'subject': forms.TextInput(attrs={
                'placeholder': 'Subject'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': (
                    'Tell me about your project, opportunity,'
                    'or inquiry...'
                ),
                'rows': 6
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            existing_classes = field.widget.attrs.get('class','')

            field.widget.attrs['class'] = (
                f'{existing_classes} {self.base_classes}'
            ).strip()

    def clean_name(self):
        name = self.cleaned_data['name'].strip()

        return name
    
    def clean_subject(self):
        subject = self.cleaned_data['subject'].strip()

        return subject