from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

# Create your views here.
from .models import *
from .forms import OwnerForm, CreateUserForm, DogsForm
#from .filters import OwnerFilter
from .decorators import unauthenticated_user, allowed_users, admin_only


# @unauthenticated_user
def home (request):
    return render (request, 'accounts/main.html')

@unauthenticated_user
def registerPage(request):

	form = CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			username = form.cleaned_data.get('username')

			group = Group.objects.get(name='owner')
			user.groups.add(group)
			#Added username after video because of error returning customer name if not added
			Owner.objects.create(
				user=user,
				name=user.username,
				)

			messages.success(request, 'Account was created for ' + username)

			return redirect('login')
		

	context = {'form':form}
	return render(request, 'accounts/register.html', context)

@unauthenticated_user
def loginPage(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.info(request, 'Username OR password is incorrect')

	context = {}
	return render(request, 'accounts/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['owner'])
def accountSettings(request):
	owner = request.user.owner
	form = OwnerForm(instance=owner)

	if request.method == 'POST':
		form = OwnerForm(request.POST, request.FILES,instance=owner)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'accounts/account_settings.html', context)




@login_required(login_url='login')
@allowed_users(allowed_roles=['owner'])
def dogs(request):
	dogs = Dogs.objects.all()

	return render(request, 'accounts/products.html', {'products':dogs})

@login_required(login_url='login')
@allowed_users(allowed_roles=['owner'])
def owner(request, pk_test):
	owner = Owner.objects.get(id=pk_test)

	dogs = owner.order_set.all()
	dog_count = dogs.count()

	context = {'customer':owner, 'orders':dogs, 'order_count':dog_count}
	return render(request, 'accounts/customer.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['owner'])
def createDog(request, pk):
	OrderFormSet = inlineformset_factory(Owner, Dogs, fields=('product', 'status'), extra=10 )
	owner = Owner.objects.get(id=pk)
	formset = OrderFormSet(queryset=Dogs.objects.none(),instance=owner)
	#form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = DogsForm(request.POST)
		formset = OrderFormSet(request.POST, instance=owner)
		if formset.is_valid():
			formset.save()
			return redirect('/')

	context = {'form':formset}
	return render(request, 'accounts/order_form.html', context)