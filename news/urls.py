from django.conf.urls.defaults import patterns

urlpatterns = patterns('news.views',
    (r'^$', 'news'),
)
