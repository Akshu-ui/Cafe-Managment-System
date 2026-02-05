# Define the menu of restaurant
menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 60,
    'Salad': 70,
    'Coffee': 80
}

# Greet the customer
print("Welcome to PYTHON Restaurant")
print("Pizza: Rs40")
print("Pasta: Rs50")
print("Burger: Rs60")
print("Salad: Rs70")
print("Coffee: Rs80")

order_total = 0

# Take first order
item_1 = input("Please enter the item you want to order = ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"{item_1} added to your order")
else:
    print(f"Ordered item {item_1} is not available!")

# Ask for another item (INPUT FIRST)
another_order = input("Do you want to order another item? (Yes/No) = ")

# THEN compare
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"{item_2} added to your order")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"Total amount to pay = Rs {order_total}")
