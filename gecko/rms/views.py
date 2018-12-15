from random import randint
from django.http import (HttpResponseRedirect, JsonResponse)
from django.views import generic as g
from django.shortcuts import render
from .forms import HistoryDataForm
from .models import (AGE_RANGE,
                     GENDER_CHOICES,
                     SMOKING_CHOICES,
                     ALCOHOL_CHOICES,
                     HistoryData)

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

class HistoryDataView(g.FormView):
    form_class = HistoryDataForm
    template_name = 'UserForm.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


def get_info(r1, r2):
   lac = 10**5
   k = 1000
   const = 5*k
   r = r1 + r2
   return JsonResponse({
       'chart': [
           ['Category', 'Count'],
           ['Alive', lac],
           ['Approve', lac*r1],
           ['Reject', lac*r2],
       ],
       'table': [
           ['1 lack', lac*r, lac*r*5+const],
           ['5 lack', 5*lac*r, 5*lac*r*5+const],
           ['15 lack', 15*lac*r, 15*lac*r*5+const],
           ['50 lack', 50*lac*r, 50*lac*r*5+const],
           ['1 crore', 100*lac*r, 100*lac*r*5+const],
       ],
   }, safe=True)

def run_get_info(request, **kwargs):
    r1 = randint(20,100)/100000.
    r2 = r1*randint(1,3)/10.
    return get_info(r1, r2)

def another_run_get_info(request, **kwargs):
    if request.method == "POST":
      if 'age' in kwargs:
        age = kwargs.pop('age')
        kwargs['age__range'] = age.split(' - ')#(age-5, age+5)
      qs = HistoryData.objects.filter(**kwargs)
      total = qs.count()
      no_claim = qs.filter(claimed=1).count()
      approve = qs.filter(claimed=2).count()
      reject = qs.filter(claimed=3).count()
      r1 = approve / total
      r2 = reject / total
      return get_into(r1, r2)
    return get_into(0, 0)
