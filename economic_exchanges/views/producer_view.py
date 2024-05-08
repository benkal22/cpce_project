from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from economic_exchanges.forms import ProducerRegistrationForm
from django.views.generic import CreateView

class ProducerRegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = ProducerRegistrationForm
    success_url = reverse_lazy('dashboard')
    #Champ de redirection
    redirect_field_name = 'next'

    def get_success_url(self) -> str:
        redirect_to = self.request.GET.get(self.redirect_field_name)
        if redirect_to:
            return redirect_to
        return super().get_success_url()
