from rest_framework import serializers
from .models import Pizza, Type, Size, Topping

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ('id', 'name')


class PizzaSerializer(serializers.ModelSerializer):

    size_name = serializers.ReadOnlyField(source='size.name')
    type_name = serializers.ReadOnlyField(source='type.name')
    toppings_names = ToppingSerializer(source="topping", read_only=True, many=True)

    class Meta:
        model = Pizza
        fields = ('id', 'name', 'size_name', 'type_name', 'toppings_names')


class PizzaCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pizza
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = '__all__'

class ToppingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = '__all__'




