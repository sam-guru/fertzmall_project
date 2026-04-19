from django import forms
from django.contrib.auth.models import User


class SearchForm(forms.Form):
    query = forms.CharField(label='Search')


class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields =['username', 'first_name', 'last_name', 'email']


	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Passwords don\'t match.')
		return cd['password2']
	


class LoginForm(forms.Form):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'appearance-none border rounded w-full py-2 px-3 mb-3 leading-tight focus:outline-none focus:shadow-outline'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'appearance-none border rounded w-full py-2 px-3 mb-3 leading-tight focus:outline-none focus:shadow-outline'}))
      
