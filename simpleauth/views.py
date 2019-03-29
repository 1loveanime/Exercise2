from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm

# welcome page for logged in users
@login_required
def welcome(request):
	return render(request, 'simpleauth/welcome.html')

# registration page
def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})