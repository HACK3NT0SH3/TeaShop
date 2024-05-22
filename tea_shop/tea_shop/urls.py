"""
URL configuration for tea_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include('testapp.urls')),
    path('about_us', include('testapp.urls')),
    path('delivery', include('testapp.urls')),
    path('payment', include('testapp.urls')),
    path('catalog', include('testapp.urls')),
    path('cart', include('testapp.urls')),
    path('item', include('testapp.urls')),
    path('login', include('testapp.urls')),
    path('signup', include('testapp.urls')),
    path('Next', include('testapp.urls')),
]
