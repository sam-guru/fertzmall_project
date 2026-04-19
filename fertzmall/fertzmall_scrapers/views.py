from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import SearchForm, LoginForm, UserRegistrationForm
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse


#function to handle display of products
def product_list(request):
    # Get the sort parameter from the query string
    sort_by = request.GET.get('sort', 'name')  # Default to sorting by product name
    if sort_by == 'price_asc':
        products = Product.objects.order_by('price')
    elif sort_by == 'price_desc':
        products = Product.objects.order_by('-price')
    else:
        products = Product.objects.all()


    paginator = Paginator(products, 30)  # Show 30 products per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request, 'product_list.html', {'page_obj': page_obj})

#function to handle searching through product list
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def search_results(request):
    form = SearchForm(request.GET)
    query = None
    results = []

    if form.is_valid():
        query = form.cleaned_data.get('query')
        results = Product.objects.filter(name__icontains=query)
        
        # Sorting logic
        sort_by = request.GET.get('sort', 'name')  # Default to sorting by product name
        if sort_by == 'price_asc':
            results = results.order_by('price')
        elif sort_by == 'price_desc':
            results = results.order_by('-price')
    
    # Pagination logic
    paginator = Paginator(results, 30)  # Show 30 results per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'search_results.html', {'results': page_obj, 'query': query, 'form': form})


#user registration
def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            #Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            #Set the chosen password
            new_user.set_password( user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/dashboard.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})

def logged_out(request):
    return render(request, 'registration/logged_out.html')


#user dashboard
@login_required
def dashboard(request):
    username = request.user.username
    return render(request, 'registration/dashboard.html', {'username': username})

