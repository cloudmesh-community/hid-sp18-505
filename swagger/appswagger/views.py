from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """ Landing page """

    template_name = 'appswagger/templates/index.html'
