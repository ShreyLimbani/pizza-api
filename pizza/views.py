from django.shortcuts import render 
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from pizza.models import Pizza, Order, Shape, Size, Topping
from pizza.serializers import PizzaSerializer, OrderSerializer, ShapeSerializer, SizeSerializer, ToppingSerializer


@api_view(['GET','POST'])
def pizza_list(request, format=None):
    if request.method == 'GET':
        pizzas = Pizza.objects.all()
        serializer = PizzaSerializer(pizzas, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PizzaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    else:
        return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def pizza_detail(request, name, format=None):

    try:
        pizza = Pizza.objects.get(name=name)
    except Pizza.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = PizzaSerializer(pizza)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = PizzaSerializer(pizza, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        pizza.delete()
        return Response("Pizza Deleted",status=status.HTTP_204_NO_CONTENT)
    else:
        return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def shape_list(request, format=None):
    if request.method == 'GET':
        shapes = Shape.objects.all()
        serializer = ShapeSerializer(shapes, many=True)
        return Response(serializer.data)

    else:
        return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def shape_detail(request, name, format=None):

    try:
        shape = Shape.objects.get(name=name)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ShapeSerializer(shape)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ShapeSerializer(shape, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        shape.delete()
        return Response("Shape Deleted",status=status.HTTP_204_NO_CONTENT)
    
    else:
        return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def size_list(request, format=None):
    if request.method == 'GET':
        sizes = Size.objects.all()
        serializer = SizeSerializer(sizes, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SizeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    else:
        return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def size_detail(request, name, format=None):

    try:
        size = Size.objects.get(name=name)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = SizeSerializer(size)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = SizeSerializer(size, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        size.delete()
        return Response("Size Deleted", status=status.HTTP_204_NO_CONTENT)
    
    else:
        return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def topping_list(request, format=None):
    if request.method == 'GET':
        toppings = Topping.objects.all()
        print(toppings)
        serializer = ToppingSerializer(toppings, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ToppingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    else:
        return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def topping_detail(request, name, format=None):

    try:
        topping = Topping.objects.get(name=name)
    except topping.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ToppingSerializer(topping)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = ToppingSerializer(topping, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        topping.delete()
        return Response("Topping Deleted", status=status.HTTP_204_NO_CONTENT)
    
    else:
        return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def order_list(request):
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        print(request.data['pizza'])
        #Get Pizza
        try:
            pizza = Pizza.objects.get(name=request.data['pizza'])
        except:
            return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)    

        #Get Size
        try:
            size = Size.objects.get(name=request.data['size'])
        except:
            return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)    

        #Get Shape
        try:
            shape = Shape.objects.get(name=request.data['shape'])
        except:
            return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)    

        #Get Toppings
        toppings_name = request.data['topping'].split(',')
        toppings = list()
        for t in toppings_name:
            try:
                topping = Topping.objects.get(name=t.strip())
                toppings.append(topping.id)
            except:
                return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)    

        try:
            order = Order(user_id=None, pizza=pizza, shape= shape, size= size)
            serializer = OrderSerializer(order)
            order.save()
            order.toppings.set(toppings)
            order.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    else:
        return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def order_detail(request, pk, format=None):

    try:
        order = Order.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = OrderSerializer(order)
        return Response(serializer.data)

    elif request.method == "PUT":
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        order.delete()
        return Response("Order Deleted", status=status.HTTP_204_NO_CONTENT)
    
    else:
        return Response("Invalid Request", status=status.HTTP_400_BAD_REQUEST)