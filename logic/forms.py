from .models import Posts
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True, widget=forms.EmailInput(attrs={'class': 'input-val bg-transparent form-control form-control-lg mt-3'}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields['password2'].widget.attrs['class'] = 'input-val bg-transparent  form-control form-control-lg mt-3'
        self.fields['username'].widget.attrs['class'] = 'input-val bg-transparent form-control form-control-lg mt-3'
        self.fields['password1'].widget.attrs['class'] = 'input-val bg-transparent form-control form-control-lg mt-3'

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LoginForm(forms.ModelForm):
    username = forms.CharField(
        max_length=80)
    password = forms.CharField(
        widget=forms.PasswordInput())
    # required_css_class = 'required d-none'
    username.widget.attrs.update(
        {'class': 'form-control form-control-lg my-3 bg-transparent', 'placeholder': 'Username'})
    password.widget.attrs.update(
        {'class': 'form-control form-control-lg my-3 bg-transparent', 'placeholder': 'Password'})

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError(
                "Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ('title', 'content','image')
    def __init__(self, *args, **kwargs):
        super(PostsForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = ' input-val m-2 form-control'
        self.fields['content'].widget.attrs['class'] = 'input-val m-2 form-control'
        self.fields['content'].widget.attrs['rows'] = "2"
        self.fields['image'].widget.attrs['class'] ='form-control m-2 '
        