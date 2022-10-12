from django.db import models


class Food(models.Model):
    description = models.CharField(max_length=200)
    fdc_id = models.IntegerField(
        db_index=True, unique=True, null=False, blank=False)

    class Meta:
        ordering = ['description']

    def __str__(self):
        return self.description


class Nutrient(models.Model):
    name = models.CharField(max_length=128)
    nutrient_id = models.IntegerField(
        db_index=True, unique=True, null=False, blank=False)
    unit_name = models.CharField(max_length=50, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class FoodNutrients(models.Model):
    food = models.ForeignKey(Food, to_field="fdc_id",
                             db_column="fdc_id", on_delete=models.CASCADE)
    nutrient = models.ForeignKey(
        Nutrient, to_field="nutrient_id", db_column="nutrient_id",  on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    unit_name = models.CharField(max_length=50, null=True)

    class Meta:
        ordering = ['nutrient']

    def __str__(self):
        return self.nutrient.name+" on "+self.food.description
