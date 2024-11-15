from django.shortcuts import render, redirect
from .forms import signUpForm, updateProfile as update_p, updateUser as update_u
from django.http import HttpResponse
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required

# Create your views here.

# signup
def signup(request):
    if request.method == 'POST':
        form = signUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return HttpResponse('wrong')
    else:
        form = signUpForm()
        data = {
            'forms': form
        }
        return render(request, 'users/sign_up.html', data)
    
# logout
@login_required
def logout(request):
    auth_logout(request)
    return render(request, 'users/logout.html')


# profile
@login_required
def profile(request):
    if request.method == 'POST':
        userform = update_u(request.POST or None, instance=request.user)
        profileform = update_p(request.POST or None, request.FILES or None, instance=request.user.profile)

        if userform.is_valid() and profileform.is_valid():
            profileform.save()
            userform.save()
            return redirect('profile')
    else:
        userform = update_u(instance=request.user)
        profileform = update_p(instance=request.user.profile)
        context = {
            'u_form': userform,
            'p_form': profileform,
        } 
    return render(request, 'users/profile.html', context)


