from django.conf.urls import patterns, include, url
from cadastro.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('cadastro.views',
url(r'^$', 'home', name='home'),
url(r'^admin/', include(admin.site.urls)),
)

