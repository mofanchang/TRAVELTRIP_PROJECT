# bookings/views/checkout.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from trips.models import Trip


@login_required
def checkout_view(request):
    cart = request.session.get('cart', [])
    trips = Trip.objects.filter(id__in=cart)
    total = sum(trip.price for trip in trips)
    return render(request, 'bookings/checkout.html', {
        'trips': trips,
        'total': total
    })
