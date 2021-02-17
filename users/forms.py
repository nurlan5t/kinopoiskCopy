from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from users.models import User

from django.utils.translation import ugettext as _

class RegisterForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            'phone_number',
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
]

    def clean(self):
        clean = super().clean()
        email = clean.get('email')
        try:
            user = User.objects.get(email=email)
            raise ValidationError('User with this email already registered')
        except User.DoesNotExist:
            pass

        password = clean.get('password')
        if password.isdigit():
            raise ValidationError('Password must not be all digit')


    def save(self, *args, **kwargs):
        user = super().save()
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

    def authenticate_user(self):
        user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])

        if user:
            return user.username
        else:
            return None
