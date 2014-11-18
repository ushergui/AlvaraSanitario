from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.core.urlresolvers import reverse_lazy

from cadastro.models import Inscricao

def home(request):
        return render(request,'index.html')