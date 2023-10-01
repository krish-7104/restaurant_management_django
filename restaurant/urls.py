from django.urls import path
from . import views
urlpatterns = [
    path('create_order/', views.create_order, name='create_order'),
    path('order_history/', views.order_history, name='order_history'),
    path('menu/', views.menu, name='menu'),
    path('', views.main_page, name='main_page'), 
]