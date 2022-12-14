from food.models import Food, FoodNutrients, Nutrient
from rest_framework.viewsets import ModelViewSet
from food.serializers import FoodSerializer, NutrientSerializer, FoodNutrientSerializer

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import pagination


class FoodViewSet(ModelViewSet):
    serializer_class = FoodSerializer
    filter_backends = [SearchFilter]
    search_fields = ['description']
    pagination_class = pagination.PageNumberPagination

    def get_queryset(self):
        queryset = Food.objects.all()
        nutrient_ids = self.request.query_params.getlist('nutrient_ids', '')
        if nutrient_ids:
            for id in nutrient_ids:
                foods = FoodNutrients.objects.filter(nutrient=id)
                food_ids = foods.values('food')
                queryset = queryset.filter(fdc_id__in=food_ids)
        return queryset
        

class NutrientViewSet(ModelViewSet):
    queryset = Nutrient.objects.all()
    serializer_class = NutrientSerializer
    filter_backends = [SearchFilter]
    search_fields = ['name']

    def get_queryset(self):
        params = self.request.query_params
        search_param = self.request.query_params.get('search','')
        if search_param or not params:
            return Nutrient.objects.all()
        return Food.objects.none()

class FoodNutrientViewset(ModelViewSet):
    serializer_class = FoodNutrientSerializer

    def get_queryset(self):
        fdc_id = self.request.query_params.get('fdc_id')
        if fdc_id is not None:
            queryset = FoodNutrients.objects.filter(food=fdc_id)
            return queryset
        return []
