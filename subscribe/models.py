# -*- coding: utf-8 -*-
from django.db import models

class ShortCourse(models.Model):
    STATES = (
        ('Opened','Aberto'),
        ('Closed','Fechado'),
    )
    name = models.CharField(verbose_name="nome", max_length=200)
    state = models.CharField(
        verbose_name="estado",
        max_length=6,
        choices=STATES,
        default="Opened"
    )
    vacancies = models.IntegerField(verbose_name="Vagas")
    vacancies_left = models.IntegerField(
        verbose_name="Vagas Restantes",
        #null=True,
        #blank=True
    )
    
    def __unicode__(self):
        return self.name
    
    #def save(self, *args, **kwargs):
    #    import ipdb;ipdb.set_trace()
    #    self.vacancies_left = self.vacancies*2
    #    super(ShortCourse,self).save(*args, **kwargs)
    
    def discount_vacancies(self):
        if self.vacancies_left > 1:
            self.vacancies_left -= 1
        elif self.vacancies_left == 1:
            self.vacancies_left -= 1
            self.state = 'Closed'
        self.save()


class Subscribe(models.Model):
    name = models.CharField(verbose_name="nome", max_length=200)
    rg = models.CharField(verbose_name="identidade", max_length=12)
    fone = models.CharField(verbose_name="Telefone", max_length=14)
    code = models.CharField(verbose_name="Matricula", max_length=15)
    email = models.EmailField(verbose_name="E-mail")
    institution = models.CharField(verbose_name="Instituiçao", max_length=30)
    first_short_course = models.ForeignKey(
        ShortCourse,
        related_name="first_short_course",
        verbose_name="1ª opção de minicurso"
    )
    second_short_course = models.ForeignKey(
        ShortCourse,
        related_name="second_short_course",
        verbose_name="2ª opção de minicurso"
    )
    
    def __unicode__(self):
        return self.name