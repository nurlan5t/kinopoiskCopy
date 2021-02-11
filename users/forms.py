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

    def validate_p(self):
        validate_p = super().clean()
        password = validate_p.get('password')
        try:
            user = User.objects.get(password=password)
            if password.isdigit():
                raise ValidationError("This password is entirely numeric")
            if password.is_numeric():
                raise ValidationError("This password is entirely numeric")
        except User.DoesNotExist:
            pass

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
