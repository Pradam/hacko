from django.urls import path
from .views import (IndexPage, ProbabilityCalculation,HistoryDataView)

urlpatterns = [
    path('', IndexPage.as_view(), name="intex"),
    path('input/', HistoryDataView.as_view(), name="input"),
    path('probability/', ProbabilityCalculation.as_view(), name="probability"),

]
