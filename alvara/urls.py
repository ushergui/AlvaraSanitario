from django.conf.urls import patterns, include, url
from cadastro.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('cadastro.views',
	url(r'^$', 'home', name='home'),
	url(r'^cadastro/$', Criar.as_view(), name='cadastro'),
	url(r'^lista/$', Lista.as_view(), name='lista'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^i18n/', include('django.conf.urls.i18n')),
)

