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
    )
    
    def __unicode__(self):
        return self.name
    
    def discount_vacancies(self):
        if self.vacancies_left > 1:
            self.vacancies_left -= 1
        elif self.vacancies_left == 1:
            self.vacancies_left -= 1
            self.state = 'Closed'
        self.save()


class Subscribe(models.Model):
    name = models.CharField(verbose_name="nome", max_length=200)
    rg = models.CharField(verbose_name="identidade",
        max_length=12,
        unique=True,
        help_text="Digite apenas números."
    )
    fone = models.CharField(verbose_name="Telefone",
        max_length=10,
        help_text="Digite apenas números."
    )
    code = models.CharField(verbose_name="Matricula",
        max_length=15,
        unique=True,
        blank=True,
        null=True,
        help_text="Digite apenas números. Somente para alunos do IFF."
    )
    email = models.EmailField(verbose_name="E-mail")
    institution = models.CharField(verbose_name="Instituição", max_length=30)
    first_short_course = models.ForeignKey(
        ShortCourse,
        blank=True,
        null=True,
        related_name="first_short_course",
        verbose_name="1ª opção de minicurso"
    )
    second_short_course = models.ForeignKey(
        ShortCourse,
        blank=True,
        null=True,
        related_name="second_short_course",
        verbose_name="2ª opção de minicurso"
    )
    
    def __unicode__(self):
        return self.name