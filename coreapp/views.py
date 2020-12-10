from .models import Pizza, Type, Size, Topping
from .serializers import PizzaSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class PizzaList(APIView):
    """
    List all pizzas, or create a new pizza.
    """
    def get(self, request, format=None):
        pizzas = Pizza.objects.all()
        serializer = PizzaSerializer(pizzas, many=True)
        return Response(serializer.data)

    # def post(self, request, format=None):
    #     serializer = PizzaSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)