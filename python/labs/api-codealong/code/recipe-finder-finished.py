ingredients = []

enter_more = input("Do you have any specific ingredients to enter? [y|n]:").lower()

while enter_more == "y":
    ingredients.append(input("What is the ingredient? One word only please:").lower())
    enter_more = input("Do you have any more ingredients to enter? [y|n]:").lower()

recipe_type = input("What kind of recipe do you want to find?")

# Write your code below!

ingredient_string = ",".join(ingredients)

import requests

url = "http://www.recipepuppy.com/api/?i=%s&q=%s" % (ingredient_string, recipe_type)
res = requests.get(url)
print(type(res.status_code))

recipes = res.json()["results"]

print("Your results:")
for i in range(len(recipes)):
    recipe = recipes[i]
    print("%s: %s" % (i, recipe["title"]))

choice = int(input("Choose a recipe (number): "))

print("Great choice!  You can find that recipe here:")
print(recipes[choice]["href"])