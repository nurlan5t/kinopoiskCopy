
from django.urls import path
from . import views

urlpatterns = [
    path('wiki/', views.WikipediaView.as_view()),
    path('translator/', views.TranslatorView.as_view()),

]