

from django.shortcuts import render
from .models import FoodItem, FoodOrder

def food_list(request):
    foods = FoodItem.objects.all()
    orders = FoodOrder.objects.all()

    return render(request, 'food/food_list.html', {
        'foods': foods,
        'orders': orders,
    })

