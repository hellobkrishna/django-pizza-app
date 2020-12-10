from .models import Pizza, Type, Size, Topping
from .serializers import PizzaSerializer, PizzaCreateSerializer
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




class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)