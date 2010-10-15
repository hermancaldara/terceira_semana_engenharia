from django.shortcuts import render_to_response
from django.template import RequestContext
from news.models import News

def index(request):
    latest_news = News.objects.all()[:5]
    return render_to_response(
        'index.html',
        {'latest_news':latest_news},
        context_instance=RequestContext(request)
    )
