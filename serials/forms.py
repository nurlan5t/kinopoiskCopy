from django import forms

from users.models import User
from .models import Comment, Serial


class CommentForm(forms.ModelForm):
    serial = forms.ModelChoiceField(widget=forms.HiddenInput(),
                                    disabled=True, required=False, queryset=Serial.objects.all())
    user = forms.ModelChoiceField(widget=forms.HiddenInput(), disabled=True, queryset=User.objects.all(),
                                  required=False)

    class Meta:
        model = Comment
        fields = ['text', 'serial', 'user']
