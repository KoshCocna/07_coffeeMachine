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
profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
is_on = True


def is_resources_sufficient(order_ingredients):
    """Return True if ingredients are sufficient, if not return False"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry, We don't have enough {item}")
            return False
    return True


def process_coin():
    """Return total coin that the customer paid"""
    print("Pls insert coins")
    total = 0
    total = int(input("Pls insert quarters: ")) * 0.25
    total += int(input("Pls insert dimes: ")) * 0.1
    total += int(input("Pls insert nickels: ")) * 0.05
    total += int(input("Pls insert pennies: ")) * 0.01
    return total


def recalc_resources(ingredients):
    """Recalculate the resources"""
    for item in ingredients:
        resources[item] -= ingredients[item]


while is_on:
    selection = input("What would you like? (espresso | latte | cappuccino):")

    if selection == "off":
        is_on = False
    elif selection == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"cost: ${profit}")
    elif selection in ["espresso", "latte", "cappuccino"]:
        drink = MENU[selection]
        if is_resources_sufficient(drink['ingredients']):
            payments = round(process_coin(), 2)
            if payments >= drink['cost']:
                profit += drink['cost']
                changes = round((payments - drink['cost']), 2)
                recalc_resources(drink['ingredients'])
                print(f"Here is your {selection}☕ and your changes are {payments}$ - {drink['cost']}$ = {changes}$")
            else:
                print(f"{selection} costs {drink['cost']}$, your payment is {payments}$ so we refund your coins.")
                payments = 0
    else:
        print("Ops, I guess there is a typo, Pls try again.")
