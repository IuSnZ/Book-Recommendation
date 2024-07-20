from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created! You are now able to login !')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form':form})

@login_required
def profile(request):
    return render(request, 'user/profile.html')

def user_profile(request, id):
    user = User.objects.get(id=id)
    if user:
        return render(request, 'user/user_profile.html', context={'user': user})
    
    return redirect('home')