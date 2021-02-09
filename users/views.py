from django.shortcuts import render
from django.views import generic

# Create your views here.
class RegisterView(generic.CreateView):
    def post(self):