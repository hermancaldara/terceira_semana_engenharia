from django.conf.urls.defaults import patterns

urlpatterns = patterns('subscribe.views',
    (r'^$', 'subscribe'),
    (r'^generate_first_short_course_options/$',
        'generate_first_short_course_options'
    ),
    (r'^generate_second_short_course_options/$',
        'generate_second_short_course_options'
    ),
    (r'^report/$', 'report'),
)
