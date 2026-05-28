from django.contrib import admin

from apps.contact.models import ContactMessage

@admin.register(ContactMessage)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'is_read')
    search_fields = ('subject','email')
    list_filter = ('is_read', 'subject')
    ordering = ('is_read', 'created_at')


