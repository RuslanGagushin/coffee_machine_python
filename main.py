import menu
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

work_on = True
my_coffee_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
menus = Menu()


while work_on:
    options = menus.get_items()
    choice = input(f"What would you like to drink? ({options})")
    if choice == "off":
        work_on = False
    elif choice == "report":
        my_coffee_maker.report()
        my_money_machine.report()
    else:
        drink = menus.find_drink(choice)
        if my_coffee_maker.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            my_coffee_maker.make_coffee(drink)