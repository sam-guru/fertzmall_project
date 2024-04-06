from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Product
from .forms import SearchForm

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