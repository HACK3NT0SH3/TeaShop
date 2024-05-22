from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class signupform(UserCreationForm):
    name = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=12)
    email = forms.CharField(max_length=50)

    class meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'name', 'phone')

    def save(self, commit=True):
        user = super(signupform, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.name = self.cleaned_data['name']
        user.phone = self.cleaned_data['phone']

        if commit:
            user.save()
        return user
