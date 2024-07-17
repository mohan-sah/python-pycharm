from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# created objects
menu = Menu()
menuitem = MenuItem('name', 'water', 'milk', 'coffee', 'cost')
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:

    # TODO: 2. Check resources sufficient ?

    choice = input(f"please choose -  {menu.get_items()} :")
    if choice == "off":
        is_on = False
    elif choice == "report":
        # TODO:1. Print report
        coffee_maker.report()
        money_machine.report()
    else:

        drink = Menu().find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            # TODO: 3. Process coins.
            # TODO: 4. Check transaction successful?
            if money_machine.make_payment(drink.cost):
                # TODO: 5. Make Coffee.
                coffee_maker.make_coffee(drink)
            else:
                print("payment not sufficient")
        else:
            print("resources not sufficient")







