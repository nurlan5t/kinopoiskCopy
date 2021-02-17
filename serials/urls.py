from django.urls import path
from . import views

urlpatterns = [
    path('', views.SerialsView.as_view()),
    path('add-serial/', views.SerialCreateView.as_view()),
    path('detail-serial/<int:pk>/', views.SerialDetailView.as_view()),
]