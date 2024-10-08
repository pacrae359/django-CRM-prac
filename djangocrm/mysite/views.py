from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.db.models import Q

from django.urls import reverse

from .forms import SignUpForm, AddRecordForm, ChangeRecordForm

from .models import Record

# Create your views here.


def home(request):

	sort_by = request.GET.get('sort_by', 'last_name')
	order = request.GET.get('order','desc')
	
	if order == "desc":
		records = Record.objects.all().order_by(f"-{sort_by}").values()
	else:
		records = Record.objects.all().order_by(sort_by).values()

	#Check if the request being recieved is from the login form
	if request.method == "POST":

		#Retrieve the password and username information from the form
		username = request.POST['username']
		password = request.POST['password']
		#Check if a user exists with matching credentials
		user = authenticate(request, username = username, password = password)
		#If a user did exists then login the user and redirect to the home page
		if user is not None:
			login(request, user)
			messages.success(request, 'You have successfully logged in!')
			return redirect(reverse('home'))
		else:
			messages.warning(request, 'This Password and Username combination does not exist!')
			return redirect(reverse('home'))

	else:
		return render(request, 'index.html', {'records':records, 'sort_by':sort_by , 'order':order})

def search_record(request):
	if request.user.is_authenticated:
		if request.method=="POST":
			searched = request.POST['searched']
			#Check if the search matches any factor of any record in the database, if so, show those in the search results.
			records = Record.objects.filter(
				Q(last_name__icontains=searched)|Q(first_name__icontains=searched)|Q(email__icontains=searched)|Q(phone__icontains=searched)|Q(address__icontains=searched)|Q(city__icontains=searched)|Q(state__icontains=searched)|Q(post_code__icontains=searched)
				).values()
			if records:
				return render(request, 'search_record.html', {'searched': searched , 'records':records})
			else:
				messages.warning(request, "The search yielded no results!")
				return redirect(reverse('home'))
		messages.warning(request, "Please enter a search query before going to the search page!")
		return redirect(reverse('home'))
	else:
		messages.warning(request, 'You are not authorised to access that page!')
		return redirect(reverse('home'))

def delete_record(request,pk):
	if request.user.is_authenticated:
		if request.method=="POST":
			record = Record.objects.get(id=pk)
			record.delete()
			messages.success(request, 'The selected record has been deleted successfully!')
			return redirect(reverse('home'))

def individual_record(request,pk):
	if request.user.is_authenticated:
		record = Record.objects.get(id=pk)
		return render(request, 'individual_record.html', {'record':record})
	else:
		messages.warning(request, 'You must be logged in to access this page!')
		return redirect(reverse('home'))

def add_record(request):
	if request.user.is_authenticated:
		if request.method=="POST":
			form = AddRecordForm(request.POST)
			if form.is_valid():
				form.save()
			return redirect(reverse('home'))
		else:
			form = AddRecordForm()
			return render(request, 'add_record.html', {'form':form})
	else:
		messages.warning(request, 'You must be logged in to access this page!')
		return redirect(reverse('home'))

def edit_record(request, pk):
	if request.user.is_authenticated:
		try:
			record = Record.objects.get(id=pk)
		except Record.DoesNotExist:
			messages.warning(request, 'The requested record does not exist!')
			return redirect(reverse('home'))
		if request.method=="POST":
			form = ChangeRecordForm(request.POST, instance=record)
			if form.is_valid:
				form.save()
				messages.success(request, "You have updated that record successfully!")
				return redirect(reverse('home'))
		else:
			form = ChangeRecordForm(instance=record)
			return render(request,'edit_record.html',{'form':form, 'record':record})
	else:
		messages.warning(request, 'You must be logged in to access this page!')
		return redirect(reverse('home'))

	messages.warning(request, 'That record does not exist!')
	return redirect(reverse('home'))

def logout_user(request):
	logout(request)
	messages.success(request, 'You have logged out!')
	return redirect(reverse('home'))

def register_user(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(request, username=username, password=password)
			login(request, user)
			messages.warning(request, "You Have Registered Successfully!")
			return redirect(reverse('home'))
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})
	
