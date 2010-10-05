# -*- coding: utf-8 -*-
from django.db import models

class ShortCourse(models.Model):
    name = models.CharField(verbose_name="name", max_length=200)
    
    def __unicode__(self):
        return self.name


class Subscribe(models.Model):
    name = models.CharField(verbose_name="nome", max_length=200)
    rg = models.CharField(verbose_name="identidade", max_length=12)
    fone = models.CharField(verbose_name="Telefone", max_length=14)
    id_ = models.CharField(verbose_name="Matricula", max_length=15)
    email = models.EmailField(verbose_name="E-mail")
    institution = models.CharField(verbose_name="Instituiçao", max_length=30)
    first_short_course = models.ForeignKey(ShortCourse)
    second_short_course = models.ForeignKey(ShortCourse)
    
    def __unicode__(self):
        return self.name