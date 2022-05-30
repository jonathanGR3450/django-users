from django.urls import path
from .views import HomeTemplateView, SampleTemplateView

urlpatterns = [
    path('', HomeTemplateView.as_view(), name="home"),
    path('sample/', SampleTemplateView.as_view(), name="sample"),
]