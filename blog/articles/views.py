# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .models import Article 

# Create your views here.
#from django.http import HttpResponse


def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'index.html', context)