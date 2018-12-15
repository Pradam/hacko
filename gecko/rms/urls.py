from django.urls import path
from .views import (IndexPage, ProbabilityCalculation)

urlpatterns = [
    path('', IndexPage.as_view(), name="index"),
    path('probability/', ProbabilityCalculation.as_view(), name="probability"),
]
