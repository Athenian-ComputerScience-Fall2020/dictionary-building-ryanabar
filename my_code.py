# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#  stackoverflow


store_list = []

while (True):
    name = input("Give the name of the owner of the store you want to add: ")
    customers = input("Total number of customers per day (seperated by spaces): ").split(" ")
    sales = input("Total number of sales per day (seperated by spaces): ").split(" ")
    staff = input("Total number of staff per day (seperated by spaces): ").split(" ")

    store_list.append({
        "name": name,
        "customers": customers,
        "sales": sales,
        "staff": staff
    })

    cont = input("Want to add another store? Please say yes or no. ")
    if cont == "no":
        break;
    elif cont == "No":
        break;

print(store_list)