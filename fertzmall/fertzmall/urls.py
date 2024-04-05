from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from fertzmall_scrapers.views import search_results
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Include Django's authentication URLs
    path('', include('fertzmall_scrapers.urls')),
    path('search/', search_results, name='search_results'),

    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
