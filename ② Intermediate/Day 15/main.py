# Python script for a coffee machine
# Turns off when there are no resources left in the machine

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
}

quarter = 0.25
dime = 0.10
nickel = 0.05
penny = 0.01
can_continue = True

while can_continue:
    print("\n☕ Coffee machine ☕\n")
    print("(You can type 'report' to see how much resources are left in the machine.)")
    coffee = input("What would you like? Choose one: espresso, latte, cappuccino. ").lower()

    if coffee == 'report':
        for key in resources:
            print(f"{key}: {resources[key]}")
    elif coffee == 'espresso' or coffee == 'latte' or coffee == 'cappuccino':
        print("\nPlease insert coins.\n")
        quarters = float(input("How many quarters? "))
        dimes = float(input("How many dimes? "))
        nickels = float(input("How many nickels? "))
        pennies = float(input("How many pennies? "))
        total = quarters * quarter + dimes * dime + nickels * nickel + pennies * penny
        drink = MENU[coffee]
        cost = drink["cost"]
        enough_resources = True

        for ingredient in drink["ingredients"]:
            check_enough = resources[ingredient] - drink["ingredients"][ingredient]
            if check_enough >= 0:
                resources[ingredient] = resources[ingredient] - drink["ingredients"][ingredient]
            else:
                enough_resources = False
                break

        if total < cost:
            print("Sorry, that's not enough money. Money refunded.")
        elif not enough_resources:
            print(f"Sorry, there's not enough resources for your {coffee}. Money refunded.")
        else:
            print(f"\n${'%0.2f'%(total - cost)} is your change.")
            print(f"Here is your {coffee}. Enjoy!")

        if resources["water"] < 50 or resources["coffee"] < 18:
            print("Sorry, we're out of resources. Come back later.")
            can_continue = False
    else:
        print("Invalid input.")
