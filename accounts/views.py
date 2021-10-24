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
from .forms import  CreateUserForm, OwnerForm, DogsForm, VolunteerForm
# from .filters import OrderFilter
# from .decorators import unauthenticated_user, allowed_users, admin_only
# import json


# data = json.dumps({ 'participant_specific_donation' : info , 'participant_specific_milestone' : info1 })

# @unauthenticated_user
def home (request):
    return render (request, 'accounts/1MainPageWT.html')

def SignupPM (request):
	if request.method == 'POST':
		username = request.POST ['username']
		email = request.POST ['email']
		password = request.POST ['password']
		confirm_password = request.POST ['confirm_password']
		if password == confirm_password:
			if User.objects.filter (email = email).exists():
				messages.info (request, 'Email already exists.')
				return redirect ('SignupPM')
			elif User.objects.filter (username = username).exists():
				messages.info (request, 'Username already exists.')
				return redirect ('SignupPM')
			else:
				user = User.objects.create_user (username = username, email = email, password = password) 
				user.save();
				group = Group.objects.get(name='Owner')
				user.groups.add(group)
				Owner.objects.create(user=user,name=user.username,)
				messages.info (request, 'Account created successfully, login now!')
				return redirect ('memberarea')

		else:
			messages.info (request, 'Incorrect Password.')
			return redirect ('SignupPM')
	else:
		return render (request, 'accounts/2-1SignupPM.html')


def SignupV (request):
	if request.method == 'POST':
		username = request.POST ['username']
		email = request.POST ['email']
		password = request.POST ['password']
		confirm_password = request.POST ['confirm_password']

		if password == confirm_password:
			if User.objects.filter (email = email).exists():
				messages.info (request, 'Email already exists.')
				return redirect ('SignupV')
			elif User.objects.filter (username = username).exists():
				messages.info (request, 'Username already exists.')
				return redirect ('SignupV')
			else:
				user = User.objects.create_user (username = username, email = email, password = password)
				user.save();
				group = Group.objects.get(name='Volunteer')
				user.groups.add(group)
				Volunteer.objects.create(user=user,name=user.username,)
				messages.info (request, 'Account created successfully, login now!')
				return redirect ('vmemberarea')
		else:
			messages.info (request, 'Incorrect Password')
			return redirect ('SignupV')
	else:
		return render (request, 'accounts/2-2SignupV.html') 



# @unauthenticated_user
# def SignupPM(request):

# 	form = CreateUserForm()
# 	if request.method == 'POST':
# 		form = CreateUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			username = form.cleaned_data.get('username')

# 			# group = Group.objects.get(name='customer')
# 			# user.groups.add(group)
# 			#Added username after video because of error returning customer name if not added
# 			Owner.objects.create(
# 				user=user,
# 				name=user.username,
# 				)

# 			messages.success(request, 'Account was created for ' + username)

# 			return redirect('loginPM')
# 		else :
# 			messages.info(request, 'Invalid credentials, Please register again.')
# 			return redirect('SignupPM')
		

# 	context = {'form':form}
# 	return render(request, 'accounts/2-1SignupPM.html', context)

# # @unauthenticated_user
# def SignupV(request):

# 	form = CreateUserForm()
# 	if request.method == 'POST':
# 		form = CreateUserForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			username = form.cleaned_data.get('username')

# 			# group = Group.objects.get(name='customer')
# 			# user.groups.add(group)
# 			#Added username after video because of error returning customer name if not added
# 			Volunteer.objects.create(
# 				user=user,
# 				name=user.username,
# 				)

# 			messages.success(request, 'Account was created for ' + username)

# 			return redirect('loginV')
# 		else :
# 			messages.info(request, 'Invalid credentials, Please register again.')
# 			return redirect('SignupV')
		
		

# 	context = {'form':form}
# 	return render(request, 'accounts/2-2SignupV.html', context)

# @unauthenticated_user
def loginPM(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('memberarea')
		else:
			messages.info(request, 'Username OR password is incorrect')
			return redirect('loginPM')

	context = {}
	return render(request, 'accounts/2-1SignupPM.html', context)

# @unauthenticated_user
def loginV(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			return redirect('vmemberarea')
		else:
			messages.info(request, 'Username OR password is incorrect')
			return redirect('loginV')

	context = {}
	return render(request, 'accounts/2-2SignupV.html', context)

# def logoutUser(request):
# 	logout(request)
# 	return redirect('login')



# @login_required(login_url='login')
# @admin_only
# def home(request):
# 	orders = Order.objects.all()
# 	customers = Customer.objects.all()

# 	total_customers = customers.count()

# 	total_orders = orders.count()
# 	delivered = orders.filter(status='Delivered').count()
# 	pending = orders.filter(status='Pending').count()

# 	context = {'orders':orders, 'customers':customers,
# 	'total_orders':total_orders,'delivered':delivered,
# 	'pending':pending }

# 	return render(request, 'accounts/dashboard.html', context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['customer'])
# def userPage(request):
# 	orders = request.user.customer.order_set.all()

# 	total_orders = orders.count()
# 	delivered = orders.filter(status='Delivered').count()
# 	pending = orders.filter(status='Pending').count()

# 	print('ORDERS:', orders)

# 	context = {'orders':orders, 'total_orders':total_orders,
# 	'delivered':delivered,'pending':pending}
# 	return render(request, 'accounts/user.html', context)


# @login_required(login_url='loginPM')
# @allowed_users(allowed_roles=['Owner'])
def ownerSettings(request):
    # owner = request.user.username
    # form = OwnerForm(instance=owner)

    # if request.method == 'POST':
    #     form = OwnerForm(request.POST, request.FILES,instance=owner)
    #     if form.is_valid():
    #         form.save()


    # context = {'form':form}
    return render(request, 'accounts/UserProfile.html')

# @login_required(login_url='loginPM')
# @allowed_users(allowed_roles=['Owner'])
def petSettings(request):
    # dog = request.user.dog
    # form = DogsForm(instance=dog)

    # if request.method == 'POST':
    #     form = DogsForm(request.POST, request.FILES,instance=dog)
    #     if form.is_valid():
    #         form.save()


    # context = {'form':form}
    return render(request, 'accounts/editPetProfile.html')


# @login_required(login_url='login')
# @allowed_users(allowed_roles=['customer'])
# def ownerSettings(request):
# 	owner = User.objects.get (user = request.id)
# 	form = OwnerForm(instance=owner)

# 	if request.method == 'POST':
# 		form = OwnerForm(request.POST, request.FILES,instance=owner)
# 		if form.is_valid():
# 			form.save()


# 	context = {'form':form}
# 	return render(request, 'accounts/UserProfile.html', context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['customer'])
# def petSettings(request):
# 	dog = User.objects.get(request.user)
# 	form = DogsForm(instance=dog)

# 	if request.method == 'POST':
# 		form = DogsForm(request.POST, request.FILES,instance=dog)
# 		if form.is_valid():
# 			form.save()


# 	context = {'form':form}
# 	return render(request, 'accounts/editPetProfile.html', context)





# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
# def products(request):
# 	products = Product.objects.all()

# 	return render(request, 'accounts/memberArea.html', {'products':products})

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
def memberArea (request):
    dogs = Dogs.objects.all()
    return render (request, 'accounts/memberArea.html', {'dogs': dogs})


def vmemberArea (request):
    return render (request, 'accounts/vmemberArea.html')


def volunteerSettings1 (request):
	return render (request, 'accounts/volunteerSignup.html')
def volunteerSettings2 (request):
	return render (request, 'accounts/volunteerSignup2.html')



# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
# def customer(request, pk_test):
# 	customer = Customer.objects.get(id=pk_test)

# 	orders = customer.order_set.all()
# 	order_count = orders.count()

# 	myFilter = OrderFilter(request.GET, queryset=orders)
# 	orders = myFilter.qs 

# 	context = {'customer':customer, 'orders':orders, 'order_count':order_count,
# 	'myFilter':myFilter}
# 	return render(request, 'accounts/customer.html',context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
# def createOrder(request, pk):
# 	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10 )
# 	customer = Customer.objects.get(id=pk)
# 	formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
# 	#form = OrderForm(initial={'customer':customer})
# 	if request.method == 'POST':
# 		#print('Printing POST:', request.POST)
# 		form = OrderForm(request.POST)
# 		formset = OrderFormSet(request.POST, instance=customer)
# 		if formset.is_valid():
# 			formset.save()
# 			return redirect('/')

# 	context = {'form':formset}
# 	return render(request, 'accounts/order_form.html', context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
# def updateOrder(request, pk):
# 	order = Order.objects.get(id=pk)
# 	form = OrderForm(instance=order)
# 	print('ORDER:', order)
# 	if request.method == 'POST':

# 		form = OrderForm(request.POST, instance=order)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('/')

# 	context = {'form':form}
# 	return render(request, 'accounts/order_form.html', context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
# def deleteOrder(request, pk):
# 	order = Order.objects.get(id=pk)
# 	if request.method == "POST":
# 		order.delete()
# 		return redirect('/')

# 	context = {'item':order}
# 	return render(request, 'accounts/delete.html', context)

# @login_required(login_url='login')
# @allowed_users(allowed_roles=['admin'])
# def createDog(request, pk):
# 	OrderFormSet = inlineformset_factory(Customer, fields=('product', 'status'), extra=10 )
# 	customer = Customer.objects.get(id=pk)
# 	formset = OrderFormSet(queryset=Dogs.objects.none(),instance=customer)
# 	#form = OrderForm(initial={'customer':customer})
# 	if request.method == 'POST':
# 		#print('Printing POST:', request.POST)
# 		form = DogsForm(request.POST)
# 		formset = OrderFormSet(request.POST, instance=customer)
# 		if formset.is_valid():
# 			formset.save()
# 			return redirect('/')

# 	context = {'form':formset}
# 	return render(request, 'accounts/editPetProfile.html', context)