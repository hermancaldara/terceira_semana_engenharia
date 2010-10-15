# -*- coding: utf-8 -*-
from datetime import date
from django.db import models


class News(models.Model):
    class Meta:
        ordering = ('-id',)
        verbose_name_plural = 'News'
        
    title = models.CharField(verbose_name='Título', max_length=100)
    news_date = models.DateField(verbose_name='Data', default=date.today())
    content = models.TextField(verbose_name='Conteúdo')
    
    def __unicode__(self):
        return self.title