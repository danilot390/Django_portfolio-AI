import resend 

from django.conf import settings

resend.api_key = settings.RESEND_API_KEY

def send_contact_notification(contact_message):

    subject = f'[TRAD Contact] {contact_message.subject}'

    html_content = f"""
    <h2>TRAD - Contact Message</h2>

    <p><strong>Name:</strong> {contact_message.name}</p>

    <p><strong>Email:</strong> {contact_message.email}</p>

    <p><strong>Subject:</strong> {contact_message.subject}</p>

    <hr>

    <p><strong>Message:</strong></p>

    <p>{contact_message.message}</p>
    """

    r = resend.Emails.send({
        'from': settings.DEFAULT_FROM_EMAIL,
        'to': settings.CONTACT_RECEIVER_EMAIL,
        'subject': subject,
        'html': html_content,
        'reply_to': contact_message.email,
    })