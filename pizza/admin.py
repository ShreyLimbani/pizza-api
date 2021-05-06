from django.contrib import admin
from .models import Pizza, Shape, Size, Order, Topping

admin.site.register(Pizza)
admin.site.register(Shape)
admin.site.register(Size)
admin.site.register(Order)
admin.site.register(Topping)