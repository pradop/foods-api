

from django.urls import include, path
from rest_framework import routers
from food.views import FoodViewSet, NutrientViewSet, FoodNutrientViewset

router = routers.DefaultRouter()
router.register(r'food', FoodViewSet, basename='Food')
router.register(r'food_detail', FoodNutrientViewset, basename='FoodDetail')
router.register(r'nutrient', NutrientViewSet, basename='Nutrient')

urlpatterns = [
    path('', include(router.urls)),
]
