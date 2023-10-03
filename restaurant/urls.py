from django.urls import path
from . import views
urlpatterns = [
    path('create_order/', views.create_order, name='create_order'),
    path('order_history/', views.order_history, name='order_history'),
    path('', views.menu, name='menu'),
    path('add_menu/', views.add_menu_item, name='add_menu'),
    path('order/<int:order_id>/complete/', views.complete_order, name='complete_order')
]