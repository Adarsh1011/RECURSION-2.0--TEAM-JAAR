from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('user_name')
            form.save()
            messages.success(request, f'Account created for {user_name}!')
            return redirect('blog-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'user': request.user})

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('logout')
	else:
		if request.method == 'POST':
			user = authenticate(request, user_name=request.POST.get('username'), password=request.POST.get('password'))

			if user is not None:
                
				login(request, user)
				return redirect('blog-home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'users/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')