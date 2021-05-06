from rest_framework import serializers 
from pizza.models import Order, Pizza, Shape, Size, Topping


class PizzaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pizza
        fields = ('name', 'description')


class ShapeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shape
        fields = ('name', 'description')


class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Size
        fields = ('name', 'description')


class ToppingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Topping
        fields = ('name', 'description')


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('pizza', 'shape', 'size', 'toppings')                