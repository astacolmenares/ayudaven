from django import forms
from django.core.mail import send_mail
from django.conf import settings

class MensajeForm(forms.Form):
	desde = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','type': 'email','placeholder': 'Su correo'}))
	mensaje = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'Su mensaje'}))

	def enviar_mail(self):
		send_mail(
			'AYUDAVEN',
			self.cleaned_data['desde'] + '\n\n' + self.cleaned_data['mensaje'],
			settings.EMAIL_HOST_USER,
			['to@mail.com'],
			fail_silently=True,
		)