from django.views import generic as g
from django.shortcuts import render
from .models import (AGE_RANGE,
                     GENDER_CHOICES,
                     SMOKING_CHOICES,
                     ALCOHOL_CHOICES)

# Create your views here.

class IndexPage(g.TemplateView):
    template_name = 'index.html'


class ProbabilityCalculation(g.TemplateView):

    template_name = 'calculation.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ProbabilityCalculation, self).get_context_data(*args, **kwargs)
        context['ages'] = AGE_RANGE
        context['genders'] = GENDER_CHOICES
        context['smokings'] = SMOKING_CHOICES
        context['alcohols'] = ALCOHOL_CHOICES
        return context
