from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True, widget=forms.EmailInput(attrs={'class': 'input-val bg-transparent form-control form-control-lg my-3'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password2'].widget.attrs['class'] = 'input-val bg-transparent  form-control form-control-lg my-3'
        self.fields['username'].widget.attrs['class'] = 'input-val bg-transparent form-control form-control-lg my-3'
        self.fields['password1'].widget.attrs['class'] = 'input-val bg-transparent form-control form-control-lg my-3'

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=80)
    password = forms.CharField(widget=forms.PasswordInput())
    # required_css_class = 'required d-none'
    username.widget.attrs.update(
        {'class': 'form-control m-2 w-75 input-val', 'placeholder': 'Username'})
    password.widget.attrs.update(
        {'class': 'form-control m-2 w-75 input-val', 'placeholder': 'Password'})

    class Meta:
        model = User
        fields = ('username', 'password')
