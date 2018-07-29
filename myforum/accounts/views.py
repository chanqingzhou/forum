# accounts/views.py
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from accounts.forms import SignUpForm, EditProfileForm

# Signing up
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('../profile')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

# Profiles
def view_profile(request):
    args = {'user': request.user}
    return render(request,'registration/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('../../profile')

    else: 
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'registration/edit_profile.html', args)

# Timeline
def timeline(request):
    return render(request, 'registration/timeline.html')

