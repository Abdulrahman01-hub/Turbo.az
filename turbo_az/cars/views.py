from django.shortcuts import render, get_object_or_404
from .models import Car

def home_page(request):
    cars = Car.objects.all()
    context = {
        'cars': cars,
        'key1': 'value1',
        'key2': 'value2',
    }
    return render(request, 'home.html', context)


def search_results(request):
    query = request.GET.get('query', '') 
    brand = request.GET.get('brand', '')  
    cars = Car.objects.all()

    if query:
        cars = cars.filter(description__icontains=query)
    if brand:
        cars = cars.filter(brand__icontains=brand) 
    
    context = {'cars': cars}
    return render(request, 'search_results.html', context)

def car_detail(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    context = {
        'car': car, 
    }
    return render(request, 'car_detail.html', context)
