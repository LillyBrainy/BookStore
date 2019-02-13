from django import forms
from django.contrib.auth.models import User
from .models import Book

class SellForm(forms.ModelForm):
	class Meta:
		model = Book
		exclude = ['seller']
class Registration(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','email','password']

		widgets = {
		'password': forms.PasswordInput()
		}

class SignInForm(forms.Form):
	username=forms.CharField(required=True)
	password=forms.CharField(required=True,widget=forms.PasswordInput())