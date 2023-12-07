from django.contrib import admin
from food.models import Food,Calorie,Food_morning,Food_lunch,Food_dinner


# Register your models here.

admin.site.register(Food)
admin.site.register(Calorie)
admin.site.register(Food_morning)
admin.site.register(Food_lunch)
admin.site.register(Food_dinner)
