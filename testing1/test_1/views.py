from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegistrationForm, ChangeForm
from django.contrib.auth.models import User


# Create your views here.

def home(request):
	return render(request, "test_1/home.html")

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/home')
	else:
		form = RegistrationForm()
		args = {'form': form}
		return render(request, 'test_1/register.html', args)

def view_profile(request):
	args = {'user': request.user}
	return render(request, 'test_1/profile.html', args)

def edit_profile(request):
	if request.method == "POST":
		form = ChangeForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return HttpResponseRedirect("/profile")
	else:
		form = ChangeForm(instance=request.user)
		args = {'form': form}
		return render(request, "test_1/edit_profile.html", args)

