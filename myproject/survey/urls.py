from django.urls import path
from . import views

urlpatterns = [
    path('', views.survey_view, name='survey_form'),
    path('success/', views.survey_success, name='survey_success'),
]
