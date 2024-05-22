from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about_us', about, name='about'),
    path('delivery', delivery, name='delivery'),
    path('payment', payment, name='payment'),
    path('catalog', catalog, name='catalog'),
    path('cart', cart, name='cart'),
    path('item', item, name='item'),
    path('login', views.Login, name='login'),
    path('signup', views.signupview, name='signup'),
    path('Next', views.Next, name='Next'),

]