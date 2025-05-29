from inventory import menu, resources, banner
serve_next = True

coffee_inventory = resources


espresso = menu['espresso']['ingredients']
latte = menu['latte']['ingredients']
cappuccino = menu['cappuccino']['ingredients']

quarters = 0.25
dimes = 0.1
nickels = 0.05
pennies = 0.01

print(banner)

while serve_next:
    customer_order = input("What would you like? espresso/latte/cappuccino: ").lower()
    if customer_order == "espresso":
        if coffee_inventory["water"] < espresso["water"]:
            print("Sorry, you don't have enough water!")
            break
        else:
            coffee_inventory["water"] -= espresso["water"]
            if coffee_inventory["coffee"] < espresso["coffee"]:
                print("Sorry, you don't have enough coffee!")
                break
            else:
                coffee_inventory["coffee"] -= espresso["coffee"]
                coffee_inventory["money"] += menu["espresso"]["cost"]
                print(f"Your espresso is ready, pay ${menu["espresso"]["cost"]}")
                print(coffee_inventory)
    elif customer_order == "latte":
        if coffee_inventory["water"] < latte["water"]:
            print("Sorry, you don't have enough water!")
            break
        else:
            coffee_inventory["water"] -= latte["water"]
            if coffee_inventory["milk"] < latte["milk"]:
                print("Sorry, you don't have enough milk!")
                break
            else:
                coffee_inventory["milk"] -= latte["milk"]
                if coffee_inventory["coffee"] < latte["coffee"]:
                    print("Sorry, you don't have enough coffee!")
                    break
                else:
                    coffee_inventory["coffee"] -= latte["coffee"]
                    print(f"Your latte is ready, pay ${menu["latte"]["cost"]}")
                    print(coffee_inventory)
    elif customer_order == "cappuccino":
        if coffee_inventory["water"] < cappuccino["water"]:
            print("Sorry, you don't have enough water!")
            break
        else:
            coffee_inventory["water"] -= cappuccino["water"]
            if coffee_inventory["milk"] < cappuccino["milk"]:
                print("Sorry, you don't have enough milk!")
                break
            else:
                coffee_inventory["milk"] -= cappuccino["milk"]
                if coffee_inventory["coffee"] < cappuccino["coffee"]:
                    print("Sorry, you don't have enough coffee!")
                    break
                else:
                    coffee_inventory["coffee"] -= cappuccino["coffee"]
                    print(f"Your cappuccino is ready, pay ${menu["cappuccino"]["cost"]}")
                    print(coffee_inventory)

    print("We only accept payment in coin: ")
    payment_quarters = int(input("How many quarters?: "))
    payment_dimes = int(input("How many dimes?: "))
    payment_nickels = int(input("How many nickels?: "))
    payment_pennies = int(input("How many pennies?: "))
    total_payment = (payment_quarters * quarters) + (payment_dimes * dimes) + (payment_nickels * nickels) + (payment_pennies * pennies)
    print(f"Your total payment is ${total_payment}")
#     if customer_order == "off":
#        serve_next = False
#     elif customer_order == "report":
#         print(resources)
#
# coffee_inventory['water']
# TODO address the issue of customer change
# determine what to do when customer payment is above and below cost price.

