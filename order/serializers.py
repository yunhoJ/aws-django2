from rest_framework import serializers
from order.models import Shop, Menu,Orders, Order_foodlist


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model=Shop
        fields= '__all__'