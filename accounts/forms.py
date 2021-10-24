from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *

class OwnerForm(ModelForm):
	class Meta:
		model = Owner
		fields = '__all__'
		exclude = ['user']

class VolunteerForm(ModelForm):
	class Meta:
		model = Volunteer
		fields = '__all__'
		# exclude = ['user']


# class OrderForm(ModelForm):
# 	class Meta:
# 		model = Order
# 		fields = '__all__'


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class DogsForm(ModelForm) :
	class Meta:
		model = Dogs
		fields = '__all__'
		exclude = ['owner']
