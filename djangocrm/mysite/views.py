from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.urls import reverse

from .forms import SignUpForm

# Create your views here.


def home(request):

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
		return render(request, 'index.html', {})


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
			messages.success(request, "You Have Registered Successfully!")
			return redirect(reverse('home'))
	else:
		form = SignUpForm()
		return render(request, 'register.html', {'form':form})

	return render(request, 'register.html', {'form':form})
	
