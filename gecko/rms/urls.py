from django.urls import path
from .views import (IndexPage, ProbabilityCalculation,HistoryDataView, run_get_info)

urlpatterns = [
    path('', IndexPage.as_view(), name="intex"),
    path('input/', HistoryDataView.as_view(), name="input"),
    path('probability/', ProbabilityCalculation.as_view(), name="probability"),
    path('calculation/', run_get_info, name="calculate"),

]
