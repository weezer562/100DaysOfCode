from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    menu = Menu()
    maker = CoffeeMaker()

    choose_coffee = True

    while choose_coffee:

        coffee_choice = input(f"What Coffee would you like ({menu.get_items()}): ")

        if coffee_choice == "off":
            choose_coffee = False
            break
        elif coffee_choice == "report":
            maker.report()
            continue
        elif coffee_choice not in menu.get_items():
            print(f"Sorry we do not serve {coffee_choice}.")
            continue

        coffee = menu.find_drink(coffee_choice)

        if not maker.is_resource_sufficient(coffee):
            continue

        money_machine = MoneyMachine()

        complete = money_machine.make_payment(coffee.cost)

        if complete:
            maker.make_coffee(coffee)

    print("Turning off coffee machine......")


coffee_machine()
