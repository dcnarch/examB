from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('quotes', views.quotes),
    path('create_quote', views.create_quote),
    path('delete_quote', views.delete_quote),
    path('myaccount', views.update),
    path('user/<int:user_id>', views.quote_page)
]