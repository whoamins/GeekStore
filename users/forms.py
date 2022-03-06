from django.contrib.auth.forms import AuthenticationForm
from django import forms

from users.models import User


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():   # WTF
            field.widget.attrs['class'] = 'form-control py-4'

    username = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Username'}),
        min_length=1, max_length=50)
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': 'Password'}),
        min_length=1, max_length=128)

    class Meta:
        model = User
        fields = ('username', 'password')

