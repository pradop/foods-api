from food.models import Nutrient
import csv


def load_nutrient():
    with open('foodData/nutrient.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Nutrient.objects.all().delete()


        for row in reader:
            print(row)


            nutrient = Nutrient(nutrient_id=row[0],name=row[1])
            nutrient.save()