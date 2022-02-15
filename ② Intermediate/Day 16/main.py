from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
can_continue = True

while can_continue:
    print("\n☕ Coffee machine ☕\n")
    print("(You can type 'report' to see how much resources are left in the machine.)")
    print("(You can type 'off' to turn off the machine.)")
    coffee = input(f"What would you like? ({menu.get_items()}): ").lower()

    if coffee == 'report':
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(coffee) != None:
        drink = menu.find_drink(coffee)
        if money_machine.make_payment(drink.cost) and coffee_maker.is_resource_sufficient(drink):
            coffee_maker.make_coffee(drink)
    elif coffee == 'off':
        can_continue = False
    else:
        print("Invalid input.")
