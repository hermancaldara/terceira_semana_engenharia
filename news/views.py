from django.shortcuts import render_to_response
from django.template import RequestContext
from news.models import News

def news(request):
    all_news = News.objects.all()
    return render_to_response(
        'news.html',
        {'all_news':all_news},
        context_instance = RequestContext(request)
    )