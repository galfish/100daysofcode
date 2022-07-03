#importing:
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

profit = 0
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        coffee_maker.is_resource_sufficient()
        money_machine.make_payment()
        if money_machine.process_coins():
            coffee_maker.make_coffee()










