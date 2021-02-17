import wikipedia
from googletrans import Translator

from django import views
# Create your views here.
from django.shortcuts import render

from .forms import WikiForm, TranslatorForm


class WikipediaView(views.generic.View):
    form_class = WikiForm

    def get(self, request, *args, **kwargs):
        return render(request, 'wiki.html', context={'form': WikiForm()})

    def post(self, request, *args, **kwargs):
        query = request.POST
        result = wikipedia.search(query['query'])

        return render(request, 'wiki.html', context={'results': result, 'form': WikiForm()})


class TranslatorView(views.generic.View):
    form_class = TranslatorForm

    def get(self, request, *args, **kwargs):
        return render(request, 'translator.html', context={'form': TranslatorForm()})

    def post(self, request, *args, **kwargs):
        word = request.POST
        print(word)
        t = Translator()
        translate = t.translate(text=word['translate'], dest='en', src='auto')
        return render(request, 'translator.html', context={'translates': translate, 'form': TranslatorForm()})