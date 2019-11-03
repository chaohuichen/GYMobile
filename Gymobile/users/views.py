from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
# Create your views here.
def logout_view(request):
    """Log the user out."""
    logout(request)
    messages.success(request,f'You have Logout!')
    return redirect('Gymobile_app:index')

def register(request):
    """register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = UserRegisterForm()
    else:
        #process completed form
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            #new_user=form.save()
            #log the user in then redirect to home page.
            username = form.cleaned_data.get('username')
            #authenticate_user = authenticate(username=new_user.username,
                #password = request.POST['password1'])
            messages.success(request,f'Your account has been created! You are now able to log in')
            #login(request,authenticate_user)
            return redirect('login')

    context = {'form':form}
    return render(request,'users/register.html',context)

@login_required
def profile(request):
    """Profile page"""
    return render(request,'users/profile.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
    'u_form': u_form,
    'p_form': p_form
    }
    return render(request,'users/edit_profile.html',context)
