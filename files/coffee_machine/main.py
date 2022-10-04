from platform import machine
from files.coffee_machine.menu import Menu, MenuItem
from files.coffee_machine.coffee_maker import CoffeeMaker
from files.coffee_machine.money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker  = CoffeeMaker()
menu = Menu()
is_on = True


coffee_maker.report()
money_machine.report()

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if (coffee_maker.is_resource_sufficient(drink)) and (money_machine.make_payment(drink.cost)):
                coffee_maker.make_coffee(drink)
                