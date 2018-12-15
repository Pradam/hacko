from django.views import generic as g
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import (GENDER_CHOICES,
                     SMOKING_CHOICES,
                     ALCOHOL_CHOICES)
from .models import HistoryData
from django.views.generic import CreateView
from .forms import HistoryDataForm
# Create your views here.

class IndexPage(g.TemplateView):
    template_name = 'index.html'


class ProbabilityCalculation(g.TemplateView):

    template_name = 'calculation.html'

#     def get_context_data(self, *args, **kwargs):
#         context = super(ProbabilityCalculation, self).get_context_data(*args, **kwargs)
#         context['ages'] = AGE_RANGE
#         context['genders'] = GENDER_CHOICES
#         context['smokings'] = SMOKING_CHOICES
#         context['alcohols'] = ALCOHOL_CHOICES
#         return context

class HistoryDataView(g.FormView):
    form_class = HistoryDataForm
    template_name = 'UserForm.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)




