#Http lib
from django.http import HttpResponse
from django.http import JsonResponse

#Models lib
from economic_exchanges.models.producers import Producer

from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail


#Forms lib
from economic_exchanges.forms.contact_forms import ContactUsForm
# from django.forms import modelformset_factory
# from ..forms.forms import ProducerForm

#Contact Form
def contact(request, pk):
    producer = get_object_or_404(Producer, pk=pk)
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                subject=f'Message from {name or 'anonyme'} via CPCE App Contact Us Form',
                message=message,
                from_email=email,
                recipient_list = ['benkalsoft@gmail.com']
            )
            return redirect('contact-sent')
    else:
        form = ContactUsForm()
    return render(request,
                  'economic_exchanges/contact/contact.html', {'form': form, 'pk':pk, 'producer': producer})

def contact_sent(request, pk):
    producer = get_object_or_404(Producer, pk=pk)
    return render(request, 'economic_exchanges/contact/contact_sent.html', {'pk':pk, 'producer': producer})
