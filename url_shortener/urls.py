from django.urls import path
from . import views

urlpatterns = [
    path('', views.shorten_url, name='shorten_url'),
    path('stats/', views.stats, name='stats'),
    path('<str:token>/', views.redirect_url, name='redirect_url'),
]

