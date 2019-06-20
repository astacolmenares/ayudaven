from django.shortcuts import render
from django.views import generic

from .forms import *

class IndexView(generic.FormView):
	template_name = 'index.html'
	form_class = MensajeForm
	success_url = '/'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		visitas = self.request.session.get('visitas',0)
		self.request.session['visitas'] = visitas + 1
		context['visitas'] = self.request.session['visitas']
		return context

	def form_valid(self,form):
		form.enviar_mail()
		return super().form_valid(form)