from dataclasses import fields
from django                         import forms
from django.contrib.auth.models     import User
from .models                        import Book

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Hasło',
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label='Powtórz hasło',
                                widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

        def clean_password2(self):
            cd = self.cleaned_data
            if cd['password'] != cd['password2']:
                raise forms.ValidationError('Hasła nie są identyczne.')
            return cd['password2']

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = (
            'title', 
            'author', 
            'cover', 
            'publisher', 
            'premiere_date', 
            'pub_date', 
            'number_of_pages',
            'photo',
        )

class BookFormDelete(forms.ModelForm):
    class Meta:
        model = Book
        fields = (
            'deleted',
        )