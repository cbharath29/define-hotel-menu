# define hotel menu
menu ={"pizza": 10.99, "burger": 8.99, "pasta": 12.99, "salad": 7.99, "soda": 1.99

}
print("Welcome to our hotel! Here is our menu:")

#greet to customer and display menu
print("welcome to our hotel! Here is our menu:")
menu = {"pizza": 10.99, "burger": 8.99, "pasta": 12.99, "salad": 7.99, "soda": 1.99}
order_total = 0
item_1 = input("Enter the first item you would like to order: ")
if item_1 in menu:
    order_total += menu[item_1]
else:
    print("Sorry, we don't have that item on the menu.")
item_2 = input("Enter the second item you would like to order: ")
if item_2 in menu:
    order_total += menu[item_2]
else:
    print("Sorry, we don't have that item on the menu.")
item_3 = input("Enter the third item you would like to order: ")
if item_3 in menu:
    order_total += menu[item_3]
else:
    print("Sorry, we don't have that item on the menu.")
print("Your total order cost is: $", round(order_total, 2))