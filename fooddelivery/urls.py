
from django.contrib import admin
from django.urls import path
from food import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.food_list, name='food_list'),
]

