from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from trips.models import Trip
from bookings.models import Booking
from decimal import Decimal

@login_required
def create_booking(request):
    cart = request.session.get('cart', [])
    trips = Trip.objects.filter(id__in=cart)

    if not trips:
        return redirect('cart_view')  # 購物車是空的

    total = sum(trip.price for trip in trips)
    booking = Booking.objects.create(
        user=request.user,
        total=Decimal(total),
        status='Pending'
    )
    
    # 你可以之後加 BookingItem 模型來儲存每個行程
    
    # 清空購物車
    request.session['cart'] = []

    return redirect('bookings:booking_detail', booking_id=booking.id)
