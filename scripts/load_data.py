from food.models import Food, FoodNutrients, Nutrient
import csv

def run():
    foods = Food.objects.all()
    if not foods.exists():
        load_food()
        load_nutrient()
        load_food_nutrient()
        print("data loaded")
    else: 
        print("data NOT loaded")


def load_food():
    with open('foodData/food.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Food.objects.all().delete()

        print("Loading food")
        for row in reader:

            nutrient = Food(description=row[2], fdc_id=row[0])
            nutrient.save()


def load_nutrient():
    with open('foodData/nutrient.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Nutrient.objects.all().delete()

        print("Loading nutrients")
        for row in reader:

            nutrient = Nutrient(name=row[1], nutrient_id=row[0])
            nutrient.save()

def load_food_nutrient():
    with open('foodData/food_nutrient.csv') as file:
        reader = csv.reader(file)
        next(reader)
        FoodNutrients.objects.all().delete()
        print("Loading food nutrients")
        count = 0
        nutrients = Nutrient.objects.all()
        nutrient_map = {}
        for nutrient in nutrients:
            nutrient_map.update({nutrient.nutrient_id:nutrient})
        foods = Food.objects.all()
        food_map = {}
        for food in foods:
            food_map.update({food.fdc_id:food})
        for row in reader:
            amount = float(row[3])
            if amount > 0:
                count = count+1
                nutrient=nutrient_map.get(int(row[2]))
                food=food_map.get(int(row[1]))
                food_nutrient = FoodNutrients(food=food, nutrient=nutrient, amount=amount)
                food_nutrient.save()
