
from django import forms


class WikiForm(forms.Form):
    query = forms.CharField()

class TranslatorForm(forms.Form):
    translate = forms.CharField()
