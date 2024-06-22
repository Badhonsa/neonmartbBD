from django.contrib import messages
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.decorators.http import require_POST
from .models import *

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html', locals())


class ProductListView(ListView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'products'

@require_POST
def add_to_cart(request, product_id):
    if 'action' not in request.POST or request.POST['action'] not in ['increase', 'decrease']:
        return HttpResponseBadRequest("Invalid action")

    action = request.POST['action']
    product = get_object_or_404(Product, id=product_id)
    cart, _ = Cart.objects.get_or_create(user=request.user, product=product)

    if action == 'increase':
        cart.quantity += 1
    elif action == 'decrease':
        if cart.quantity > 1:
            cart.quantity -= 1
        else:
            cart.delete()  # Remove item from cart if quantity becomes zero
    cart.save()
    return redirect('cart')

def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})





def product_details(request, id):
    product = Product.objects.get(id=id)
    return render(request, "Product.html", {'product': product})







def sidebar(request):
    product_all = Product_all.objects.all()
    return render(request, 'sidebar.html',{'product_all': product_all})

