from django.contrib import admin
from exercise.models import Exercise_cardio,Exercise_low,Exercise_upper,Exercise_low_l,Exercise_upper_l,Exercise_cardio_l

# Register your models here.
admin.site.register(Exercise_cardio)
admin.site.register(Exercise_upper)
admin.site.register(Exercise_low)
admin.site.register(Exercise_low_l)
admin.site.register(Exercise_cardio_l)
admin.site.register(Exercise_upper_l)