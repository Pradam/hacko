from django.views import generic as g
from django.shortcuts import render

# Create your views here.

class IndexPage(g.TemplateView):
    template_name = 'index.html'
