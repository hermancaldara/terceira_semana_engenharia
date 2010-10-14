# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from forms import SubscribeForm
from models import ShortCourse

def subscribe(request):
    subscribe_form = SubscribeForm()
    if request.method == 'POST':
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
            subscribe = subscribe_form.save(commit=False)
            first_short_course = ShortCourse.objects.get(
                id=int(request.POST.get("first_short_course"))
            )
            first_short_course.discount_vacancies()
            second_short_course = ShortCourse.objects.get(
                id=int(request.POST.get("second_short_course"))
            )
            second_short_course.discount_vacancies()
            subscribe.first_short_course = first_short_course
            subscribe.second_short_course = second_short_course
            subscribe.save()
            return render_to_response(
                'subscribe_sucessfull.html',
                context_instance = RequestContext(request)
            )
    return render_to_response(
        'subscribe.html',
        {'subscribe_form': subscribe_form},
        context_instance = RequestContext(request)
    )
    
def generate_first_short_course_options(request):
    html = u'1ª opção de minicurso: <select id="id_first_short_course" name="first_short_course">'
    html += '<option selected="selected" value="">---------</option>'
    for short_course in ShortCourse.objects.filter(state='Opened'):
        html += '<option value="%s">%s</option>' %(
            short_course.id, short_course.name
        )
    html += '</select>'
    
    return HttpResponse(html)
    
def generate_second_short_course_options(request):
    selected_short_course = request.POST.get('selected_short_course', None)
    second_short_course = []
    all_short_courses = ShortCourse.objects.filter(state='Opened')
    for short_course in all_short_courses:
        if short_course.id != int(selected_short_course):
            second_short_course.append(short_course)
    html = u'2ª opção de minicurso: <select id="id_second_short_course" name="second_short_course">'
    html += '<option selected="selected" value="">---------</option>'
    for short_course in second_short_course:
        html += '<option value="%s">%s</option>' %(
            short_course.id, short_course.name
        )
    html += '</select>'
    
    return HttpResponse(html)