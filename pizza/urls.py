from django.conf.urls import url
from django.urls import path 
from rest_framework.urlpatterns import format_suffix_patterns
from pizza import views 
 
urlpatterns = [ 
    path('pizzas/', views.pizza_list),
    path('pizzas/<str:name>', views.pizza_detail),
    path('shapes/', views.shape_list),
    path('shapes/<str:name>', views.shape_detail),
    path('sizes/', views.size_list),
    path('sizes/<str:name>', views.size_detail),
    path('toppings/', views.topping_list),
    path('toppings/<str:name>', views.topping_detail),
    path('pizza-orders/', views.order_list),
    path('pizza-orders/<int:pk>', views.order_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)