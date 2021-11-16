from django.urls import path 
from.import views

urlpatterns = [
    path('home', views.home, name='home'),
    path('haqida',views.abaut,name='about'),
    path('xizmat',views.services,name='services'),
    path('partfolyu',views.partfolio,name='partfolio'),
    path('narx',views.pricing,name='pricing'),
    path('aloqa',views.contact,name='contact')

]