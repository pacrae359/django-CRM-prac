from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Record
from django import forms
from django.forms import ModelForm

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(required=True, max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
	email = forms.EmailField(required=True, max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}))
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email','username',
			'password1', 'password2')
	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'Username'
		self.fields['username'].label = 'Username:'
		self.fields['username'].help_text="<span class='form-text text-muted small'>Required. 150 Characters or less. Letters, digits and @/./+/-/_ only.</span>"

		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = 'Password:'
		self.fields['password1'].help_text="<ul class='form-text text-muted small'><li>Your password can't be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can't be entirely numeric.</li></ul>"

		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Password'
		self.fields['password2'].label = 'Matching Password:'
		self.fields['password2'].help_text="<ul class='form-text text-muted small'><li>Enter a matching password!</li></ul>"


class AddRecordForm(ModelForm):
	class Meta:
		model = Record
		exclude = ['created_at']
	# Quick method for adding form control class to all fields in the Form, written by Gabriel Xia - https://stackoverflow.com/a/53928592
	def __init__(self, *args, **kwargs):
		super(AddRecordForm, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'

class ChangeRecordForm(ModelForm):
	class Meta:
		model = Record
		exclude = ['created_at']
	# Quick method for adding form control class to all fields in the Form, written by Gabriel Xia - https://stackoverflow.com/a/53928592
	def __init__(self, *args, **kwargs):
		super(ChangeRecordForm, self).__init__(*args, **kwargs)
		for field_name, field in self.fields.items():
			field.widget.attrs['class'] = 'form-control'