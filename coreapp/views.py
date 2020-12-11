from .models import Pizza, Type, Size, Topping
from .serializers import PizzaSerializer, PizzaCreateSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json


class PizzaList(APIView):
    """
    List all pizzas, or create a new pizza.
    """
    def get(self, request, format=None):
        pizzas = Pizza.objects.all()
        serializer = PizzaSerializer(pizzas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PizzaCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PizzaDetail(APIView):
    """
    Retrieve, update or delete a pizza instance.
    """
    def get_object(self, pk):
        try:
            return Pizza.objects.get(pk=pk)
        except Pizza.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        pizza = self.get_object(pk)
        serializer = PizzaCreateSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        pizza = self.get_object(pk)
        serializer = PizzaCreateSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        pizza = self.get_object(pk)
        pizza.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Create an API endpoint to create regular pizza and a square pizza.

class CreateRegularPizza(APIView):
    def post(self, request, format=None):
        errors_response = {
            "name":"this field is required",
            "size":"this field is required",
            "toppings":"this field is required and accepts a list"
        }
        toppings = None
        type = None
        size = None
        name = None
        try:
            name = request.data["name"]
            toppings = request.data["toppings"]
            toppings_list = toppings
            size = request.data["size"]

            size = Size.objects.get(name = size)
            type = Type.objects.get(name = "regular")



            pizza = Pizza( name = name, type_id = type.id , size = size)
            pizza.save()

            for topping in toppings:
                topping_obj = Topping.objects.get(name = topping)
                pizza.topping.add(topping_obj)
                pizza.save()
            size_name = size.name

            response = {"name":name,"size":size_name,"type": "regular","toppings": toppings_list}

            return Response(response, status=status.HTTP_201_CREATED)
        except:
            return Response(errors_response, status=status.HTTP_400_BAD_REQUEST)


class CreateSquarePizza(APIView):
    def post(self, request, format=None):
        errors_response = {
            "name":"this field is required",
            "size":"this field is required",
            "toppings":"this field is required and accepts a list"
        }
        toppings = None
        type = None
        size = None
        name = None
        try:
            name = request.data["name"]
            toppings = request.data["toppings"]
            toppings_list = toppings
            size = request.data["size"]

            size = Size.objects.get(name = size)
            type = Type.objects.get(name = "square")

            pizza = Pizza( name = name, type_id = type.id , size = size)
            pizza.save()

            for topping in toppings:
                topping_obj = Topping.objects.get(name = topping)
                pizza.topping.add(topping_obj)
                pizza.save()
            size_name = size.name

            response = {"name":name,"size":size_name,"type": "square","toppings": toppings_list}

            return Response(response, status=status.HTTP_201_CREATED)
        except:
            return Response(errors_response, status=status.HTTP_400_BAD_REQUEST)

