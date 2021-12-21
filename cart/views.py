from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from shop.models import *
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def cart_details(request, tot=0, count=0, ct_items=None,td=0):
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
        ct_items = item.objects.filter(cart=ct, active=True)
        for i in ct_items:
            tot += (i.prodt.price * i.quantity)
            count += i.quantity
            td = 100 + tot
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', {'ci': ct_items, 't': tot, 'c': count, 'tds': td})


def c_id(request):
    ct_id = request.session.session_key
    if not ct_id:
        ct_id = request.session.create()
    return ct_id


def add_cart(request, product_id):
    prod = product.objects.get(id=product_id)
    try:
        ct = cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct = cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items = item.objects.get(prodt=prod, cart=ct)
        if c_items.quantity < c_items.prodt.stock:
            c_items.quantity += 1
        c_items.save()
    except item.DoesNotExist:
        c_items = item.objects.create(prodt=prod, quantity=1, cart=ct)
        c_items.save()
    return redirect('cart_details')


def minus_cart(request, product_id):
    ct = cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(product, id=product_id)
    c_items = item.objects.get(prodt=prod, cart=ct)
    if c_items.quantity > 1:
        c_items.quantity -= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cart_details')


def cart_delete(request, product_id):
    ct = cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(product, id=product_id)
    c_items = item.objects.get(prodt=prod, cart=ct)
    c_items.delete()
    return redirect('cart_details')
