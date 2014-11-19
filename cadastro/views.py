from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy
from django.utils.translation import ugettext_lazy as _

from cadastro.models import Inscricao
from cadastro.forms import InscricaoForm

def home(request):
        return render(request,'index.html')

class Criar(CreateView):
        template_name = 'cadastro.html'
        model = Inscricao
        success_url = reverse_lazy('lista')

class Lista(ListView):
        template_name = 'lista.html'
        model = Inscricao
        context_object = ''
		
