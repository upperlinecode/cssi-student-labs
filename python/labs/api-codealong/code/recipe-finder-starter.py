ingredients = []

enter_more = input("Do you have any specific ingredients to enter? [y|n]:").lower()

while enter_more == "y":
    ingredients.append(input("What is the ingredient? One word only please:").lower())
    enter_more = input("Do you have any more ingredients to enter? [y|n]:").lower()

recipe = input("What kind of recipe do you want to find?")

# Write your code below!

