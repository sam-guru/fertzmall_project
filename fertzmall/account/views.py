from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import SearchForm, LoginForm, UserRegistrationForm


#user login
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Authenticated successfully')
            else:
                return HttpResponse('Disabledaccount')
        else:
            return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


@login_required
def dashboard(request):
    username = request.user.username
    return render(request, 'registration/dashboard.html', {'username': username})
