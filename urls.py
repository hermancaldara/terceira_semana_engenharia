from django.conf.urls.defaults import *
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'terceira_semana_engenharia.views.index'),
    (r'^subscribe/',include('terceira_semana_engenharia.subscribe.urls')),
    (r'^news/',include('terceira_semana_engenharia.news.urls')),
    (r'^site_media/(.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
)
