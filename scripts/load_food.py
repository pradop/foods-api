from food.models import Food
import csv


def load_food():
    with open('foodData/food.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Food.objects.all().delete()


        for row in reader:
            print(row)


            nutrient = Food(description=row[2], fdc_id=row[0])
            nutrient.save()