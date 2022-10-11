
from food.models import Food, Nutrient, FoodNutrients
from rest_framework import serializers


class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['description', 'fdc_id']

class NutrientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nutrient
        fields = ['name', 'nutrient_id']


class FoodNutrientSerializer(serializers.ModelSerializer):
    nutrient = NutrientSerializer()
    nutrient = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )
    class Meta:
        model = FoodNutrients
        fields = ['amount', 'nutrient', 'unit_name']