from food.models import Food, FoodNutrients, Nutrient
from rest_framework.viewsets import ModelViewSet
from food.serializers import FoodSerializer, NutrientSerializer, FoodNutrientSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import pagination


class FoodViewSet(ModelViewSet):
    serializer_class = FoodSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['description']
    search_fields = ['description']
    pagination_class = pagination.PageNumberPagination
    
    def get_queryset(self):
        queryset = Food.objects.all()
        nutrient_id = self.request.query_params.get('nutrient_id')
        if nutrient_id is not None:
            food_ids = FoodNutrients.objects.filter(
                nutrient=nutrient_id).values('food')
            queryset = queryset.filter(fdc_id__in=food_ids)
        return queryset


class NutrientViewSet(ModelViewSet):
    queryset = Nutrient.objects.all()
    serializer_class = NutrientSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']


class FoodNutrientViewset(ModelViewSet):
    serializer_class = FoodNutrientSerializer    
    def get_queryset(self):
        fdc_id = self.request.query_params.get('fdc_id')
        if fdc_id is not None:
            queryset = FoodNutrients.objects.filter(food=fdc_id)
            return queryset
        return []
