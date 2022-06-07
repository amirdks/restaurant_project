from django.contrib import admin

# Register your models here.
from contact.models import ContactUs
from utils.email_service import send_email


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'is_read_by_admin']

    def save_model(self, request, obj: ContactUs, form, change):
        if form.cleaned_data.get('response'):
            user_email = form.cleaned_data.get('email')
            reply_message = form.cleaned_data.get('response')
            send_email(subject='contact us reply from our website', to=user_email, context={'text': reply_message},
                       template_name='contact/test_email.html')
        if form.cleaned_data.get('is_read_by_admin'):
            obj.delete()
            return None
        return super(ContactUsAdmin, self).save_model(request, obj, form, change)


admin.site.register(ContactUs, ContactUsAdmin)
