from django.shortcuts import render
from trips.models import Trip

def trip_search(request):
    trips = Trip.objects.all()

    if request.method == "POST":
        destination = request.POST.get('destination', '').strip()
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        if destination:
            trips = trips.filter(city__icontains=destination)
        if start_date:
            trips = trips.filter(start_date__gte=start_date)
        if end_date:
            trips = trips.filter(end_date__lte=end_date)
            
          # ✅ 將結果渲染到一個新的結果頁面
        return render(request, 'trips/trip_search_results.html', {'trips': trips})



    return render(request, 'home.html', context)
