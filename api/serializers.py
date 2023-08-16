from rest_framework import serializers
from .models import Product
from .models import Location
from .models import ProductMovement


class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields ='__all__'

class LocationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Location
		fields ='__all__'

class ProductMovementSerializer(serializers.ModelSerializer):
	class Meta:
		model = ProductMovement
		fields ='__all__'