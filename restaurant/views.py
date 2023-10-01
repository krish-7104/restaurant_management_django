from django.shortcuts import render, redirect
from .models import MenuItem, Order

def main_page(request):
    menu_items = MenuItem.objects.all()
    return render(request, 'restaurant/index.html', {'menu_items': menu_items})

def menu(request):
    menu_items = MenuItem.objects.all()
    print(menu_items)
    return render(request, 'restaurant/menu.html', {'menu_items': menu_items})

def create_order(request):
    if request.method == 'POST':
        selected_items = request.POST.getlist('item')
        table_number = request.POST['table_number']
        order = Order.objects.create(table_number=table_number)
        order.items.set(selected_items)
        return redirect('order_history')
    
    menu_items = MenuItem.objects.all()
    return render(request, 'restaurant/create_order.html', {'menu_items': menu_items})

def order_history(request):
    orders = Order.objects.all()
    return render(request, 'restaurant/order_history.html', {'orders': orders})
