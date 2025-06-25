from django.shortcuts import render, redirect
from trips.models import Trip
from django.contrib.auth.decorators import login_required



def add_to_cart(request, trip_id):
    cart = request.session.get('cart', [])
    if trip_id not in cart:
        cart.append(trip_id)
    request.session['cart'] = cart
    return redirect('cart_view')

def cart_view(request):
    cart = request.session.get('cart', [])
    trips = Trip.objects.filter(id__in=cart)
    return render(request, 'cart/cart.html', {'trips': trips})



def remove_from_cart(request, trip_id):
    cart = request.session.get('cart', [])
    if trip_id in cart:
        cart.remove(trip_id)
        request.session['cart'] = cart  # 更新 session
        request.session.modified = True
    return redirect('cart_view')



def clear_cart(request):
    request.session['cart'] = []  # 清空購物車
    request.session.modified = True
    return redirect('cart_view')  # 回到購物車頁面