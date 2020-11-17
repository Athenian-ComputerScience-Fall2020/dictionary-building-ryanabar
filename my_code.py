# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  stackoverflow


store_list = {}

while True:
    name = input("Give the name of the restaurant: ")
    foodType = input("What food type does this restaurant serve? ")

    store_list[name] = foodType

    cont = input("Want to add another store? Please say yes or no. ")
    if cont == "no":
        break;
    elif cont == "No":
        break;

print(store_list)