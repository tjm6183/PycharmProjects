MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def the_transaction():
    global answer
    answer = input("What would you like? (espresso/latte/cappuccino): ")
    if answer == "report":
        print_report()
    elif answer == "off":
        turn_off()
    elif answer == "espresso":
        if resources["water"] < MENU["espresso"]["ingredients"]["water"]:
            print("Sorry, there is not enough water.")
            return
        if resources["coffee"] < MENU["espresso"]["ingredients"]["coffee"]:
            print("Sorry, there is not enough coffee.")
            return
    elif answer == "latte":
        if resources["water"] < MENU["latte"]["ingredients"]["water"]:
            print("Sorry, there is not enough water.")
            return
        if resources["coffee"] < MENU["latte"]["ingredients"]["coffee"]:
            print("Sorry, there is not enough coffee.")
            return
        if resources["milk"] < MENU["latte"]["ingredients"]["milk"]:
            print("Sorry, there is not enough milk.")
            return
    elif answer == "cappuccino":
        if resources["water"] < MENU["cappuccino"]["ingredients"]["water"]:
            print("Sorry, there is not enough water.")
            return
        if resources["coffee"] < MENU["cappuccino"]["ingredients"]["coffee"]:
            print("Sorry, there is not enough coffee.")
            return
        if resources["milk"] < MENU["cappuccino"]["ingredients"]["milk"]:
            print("Sorry, there is not enough milk.")
            return

    print("Please insert coins.")

    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    sum = (quarters * .25) + (dimes * .1) + (nickles * .05) + (pennies * .01)

    resources["money"] += sum

    if answer == "espresso":
        chose_espresso()
    elif answer == "latte":
        chose_latte()
    elif answer == "cappuccino":
        chose_cappuccino()

def turn_off():
    exit()


def print_report():
    print(f'Water: {resources["water"]}')
    print(f'Milk: {resources["milk"]}')
    print(f'Coffee: {resources["coffee"]}')
    print(f'Money: {resources["money"]}')
    the_transaction()

def chose_espresso():
    if resources["money"] >= MENU["espresso"]["cost"]:
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"]:
            if resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
                resources["money"] -= MENU["espresso"]["cost"]
                resources["water"] -= MENU["espresso"]["ingredients"]["water"]
                resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
            else:
                print("Sorry, there is not enough coffee.")
        else:
            print("Sorry, there is not enough water.")
    else:
        print("Sorry, that's not enough money. Money refunded.")

    print(f'Here is {round(resources["money"],2)} in change.')
    resources["money"] = 0
    print(f'Here is your espresso. Enjoy!')

    the_transaction()


def chose_latte():
    if resources["money"] >= MENU["latte"]["cost"]:
        if resources["water"] >= MENU["latte"]["ingredients"]["water"]:
            if resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
                if resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
                    resources["money"] -= MENU["latte"]["cost"]
                    resources["water"] -= MENU["latte"]["ingredients"]["water"]
                    resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
                    resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
                else:
                    print("Sorry, there is not enough milk.")
            else:
                print("Sorry, there is not enough coffee.")
        else:
            print("Sorry, there is not enough water.")
    else:
        print("Sorry, that's not enough money. Money refunded.")

    print(f'Here is {round(resources["money"],2)} in change.')
    resources["money"] = 0
    print(f'Here is your latte. Enjoy!')

    the_transaction()



def chose_cappuccino():
    if resources["money"] >= MENU["cappuccino"]["cost"]:
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"]:
            if resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
                if resources["milk"] >= MENU["cappuccino"]["ingredients"]["milk"]:
                    resources["money"] -= MENU["cappuccino"]["cost"]
                    resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
                    resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
                    resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
                else:
                    print("Sorry, there is not enough milk.")
            else:
                print("Sorry, there is not enough coffee.")
        else:
            print("Sorry, there is not enough water.")
    else:
        print("Sorry, that's not enough money. Money refunded.")

    print(f'Here is {round(resources["money"],2)} in change.')
    resources["money"] = 0
    print(f'Here is your cappuccino. Enjoy!')

    the_transaction()

the_transaction()

