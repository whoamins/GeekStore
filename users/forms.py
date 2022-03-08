from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms

from users.models import User


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():  # WTF
            field.widget.attrs['class'] = 'form-control py-4'

    username = forms.TextInput()
    password = forms.PasswordInput()

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():  # WTF
            field.widget.attrs['class'] = 'form-control py-4'

    first_name = forms.CharField()
    last_name = forms.CharField()
    username = forms.CharField(min_length=1, max_length=50)
    email = forms.EmailInput()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2')


class EditForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():  # WTF
            field.widget.attrs['class'] = 'form-control py-4'

        self.fields['image'].widget.attrs['class'] = 'custom-file-input'

    first_name = forms.TextInput()
    last_name = forms.TextInput()
    username = forms.TextInput()
    email = forms.EmailInput()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'image')
