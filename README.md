# foods-api  
This Django-based API provides information about some foods and their nutrients.  
Since this project was meant to be a challenge I decided to use the FoodData_Central_survey_food_csv_2020-10-30 database, wich provided enough data to create a demostration, avoiding huge amount of data.  
I used food, nutrients, and food_nutrients files, this allowed me to create several models and their respective endpoints with pagination and filtering, which are key features in any API.  
The API consists of 3 endpints:  
```
 - /food : listing all foods, allowing the user to filter by food name, and nutrients present in that food  
  - /food/?search=milk will list all food that contain the keyword milk
  - /food/?nutrient_ids=1108 will list all food with the nutrient 1108 (Carotene, alpha) present 
  - /food/?nutrient_ids=1108&nutrient_ids=1105 will list all food with the nutrient 1108 (Carotene, alpha) or nutrinet 1105 (Retinol) present
 - /nutrient: listing all nutrients presents in the database, allowing the user to filter by nutrient name
 - /food_detail: listing all nutrinets present in a selected food
```

Since netlify did not allowed me to deploy the api, i had to use a server owned by intermedia
