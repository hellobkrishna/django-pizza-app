from rest_framework import serializers
from .models import Pizza, Type, Size, Topping

class ToppingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topping
        fields = ('id', 'name')


class PizzaSerializer(serializers.ModelSerializer):

    size_name = serializers.ReadOnlyField(source='size.name')
    type_name = serializers.ReadOnlyField(source='type.name')
    toppins_names = ToppingSerializer(read_only=True, many=True)

    class Meta:
        model = Pizza
        fields = ('id', 'name', 'size_name', 'type_name', 'toppins_names')

