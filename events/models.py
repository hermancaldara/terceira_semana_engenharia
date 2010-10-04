# -*- coding: utf-8 -*-
from django.db import models

class Event(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=100)
    description = models.TextField(verbose_name='Descriçao', max_length=500)
    event_date = models.DateField(verbose_name='Data')
    hour = models.TimeField(verbose_name='Horário')
    local = models.CharField(verbose_name='Local', max_length=50)
    
    def __unicode__(self):
        return self.name


class Speaker(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=100)
    who_is = models.TextField('Quem é', max_length=500)
    
    def __unicode__(self):
        return self.name


class Talk(Event):
    speaker = models.ForeignKey(Speaker)


class ShortCourse(Event):
    speaker = models.ForeignKey(Speaker)