from two_factor.views import OTPRequiredMixin
from django.views.generic import TemplateView

class MySecureView(OTPRequiredMixin, TemplateView):
    template_name = 'secure_page.html'
