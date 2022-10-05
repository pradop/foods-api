from food.models import FoodNutrients
import csv


def load_food_nutrient():
    with open('foodData/food.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        FoodNutrients.objects.all().delete()


        for row in reader:
            print(row)


            nutrient = FoodNutrients(food=row[1], nutrient=row[2], amount=row[3])
            nutrient.save()