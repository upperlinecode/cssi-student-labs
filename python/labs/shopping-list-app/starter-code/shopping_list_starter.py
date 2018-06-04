choice = ""

print("Welcome to the shopping list app!")

shopping_list = []

while choice.lower() != "e":
    print("Please choose your action from the following list:")
    print("a. Add an item to the list")
    print("b. Remove an item from the list")
    print("c. Check to see if an item is on the list")
    print("d. Show all items on the list")
    print("e. exit")
    
    choice = input("Enter your choice [a|b|c|d|e]:")
    
    # Your code below! Handle the cases when the user chooses a, b, c, d, or e