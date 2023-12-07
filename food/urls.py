from django.urls import path
from .import views

app_name = 'food'

urlpatterns =[
    path('food_list/', views.food_list, name='food_list'),
    # path('food_morning/',views.search_food, name='food_morning'),
    path('food_morning/', views.food_morning, name="food_morning"),
    # path('food_lunch/', views.search_lunch, name="food_lunch"),
    # path('food_dinner/', views.search_dinner, name="food_dinner"),
    path('food_lunch/', views.food_lunch, name="food_lunch"),
    path('food_dinner/', views.food_dinner, name="food_dinner"),
    path('food/',views.calorie, name="food")

    # path('food_morning/',views.Morning, name="food_morning")

]