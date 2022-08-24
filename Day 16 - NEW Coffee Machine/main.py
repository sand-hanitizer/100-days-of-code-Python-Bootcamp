from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

shop_menu = Menu()
coffee_machine = CoffeeMaker()
money_counter = MoneyMachine()
on = True


# coffee machine start
while on:
    print("Hey! This is a coffee machine. Your options are", shop_menu.get_items())
    order = input("Your order will be: ")
    if order == "report":
        coffee_machine.report()
        money_counter.report()
    elif order == "off":
        on = False
    else:
        item = shop_menu.find_drink(order)
        if item is not None:
            money = item.cost

            if coffee_machine.is_resource_sufficient(item) and money_counter.make_payment(money):
                coffee_machine.make_coffee(item)
