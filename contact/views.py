from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings

from .models import Contact
from .forms import ContactForm


def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_object = Contact()
            contact_object.name = form.cleaned_data['name']
            contact_object.email = form.cleaned_data['email']
            contact_object.message = form.cleaned_data['message']
            contact_object.save()

            message = 'from: ' + contact_object.email + '\n\n' + contact_object.message
            try:
                send_mail(
                    "Portfolio Contact Form",
                    message,
                    settings.EMAIL_HOST_USER,
                    [settings.EMAIL_RECIPIENT]
                    )
                return HttpResponseRedirect(reverse('thanks'))
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
        else:
            return render(request, 'contact/contact_page.html', {'form': form})
    else:
        form = ContactForm()
        return render(request, 'contact/contact_page.html', {'form': form})


def thanks_page(request):
    return render(request, 'contact/thanks_page.html')
