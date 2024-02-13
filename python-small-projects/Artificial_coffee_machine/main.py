MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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


# TODO: 1.Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
def coffee_prefer():
    """give coffee preference from user / or user's input"""
    user_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_coffee == 'espresso':
        return 'espresso'
    elif user_coffee == 'latte':
        return 'latte'
    elif user_coffee == 'cappuccino':
        return 'cappuccino'
    elif user_coffee == 'report':
        print(
            f"the current resource values.\n Water: {water_in_machine}ml"
            f" \n Milk: {milk_in_machine}ml \n Coffee: {coffee_in_machine}g \n Money: ${money_in_machine}")
        coffee_prefer()
    elif user_coffee == 'off':
        return 'turned off'
    else:
        print(f"sorry, i do not follow what you said.")
        coffee_prefer()


# TODO: 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
def is_resources_sufficient(water, milk, coffee, money, coffee_ordered):
    """returns boolean if there are enough resources to make drink"""
    print(f"coffee_ordered : {coffee_ordered}")
    if water < MENU[coffee_ordered]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False
    if milk < MENU[coffee_ordered]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        return False
    if coffee < MENU[coffee_ordered]["ingredients"]["coffee"]:
        print("Sorry there is not enough coffee.")
        return False
    # if money < MENU[coffee_ordered]["cost"]:
    #     print("Sorry there is not enough money.")
    #     return False
    else:
        print("drink in making...")
        return True


# TODO: 5.Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
def process_coins(should_sufficient_resources):
    if should_sufficient_resources:
        quarters_inserted = int(input(f"insert no of quarters coin : "))
        dimes_inserted = int(input(f"insert no of dimes coin : "))
        nickles_inserted = int(input(f"insert no of nickles coin : "))
        pennies_inserted = int(input(f"insert no of pennies coin : "))
        total_money_inserted = ((QUARTER * quarters_inserted) +
                                (DIME * dimes_inserted) +
                                (NICKLE * nickles_inserted) +
                                (PENNIE * pennies_inserted))
        return round(total_money_inserted, 2)
    else:
        print('facing problem in processing coins')


# TODO: 6.Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.
def do_transaction(machine_profit):
    """take machine profit and update it, give back extra money
    """
    if user_money >= amount_required:
        print('transaction successful, \n drink in making')
        money_to_return = round(user_money - amount_required, 2)
        machine_profit += amount_required
        print(f"Here is ${money_to_return} dollars in change.")
        return machine_profit, True

    else:
        money_to_return = round(amount_required - user_money, 2)
        print(f" you still need {money_to_return} to make this transaction successful\n"
              f"Sorry that's not enough money. Money refunded.")
        return machine_profit, False


# TODO: 7.Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.
def make_coffee(container_water, container_milk, container_coffee):
    """make coffee for user and use machine resources"""
    if should_transaction_successful:
        print(f"deducting resources")
        container_water -= MENU[coffee_ordered]["ingredients"]["water"]
        container_milk -= MENU[coffee_ordered]["ingredients"]["milk"]
        container_coffee -= MENU[coffee_ordered]["ingredients"]["coffee"]
        print(f"Here is your latte. Enjoy!")
    else:
        print("cannot proceed with coffee making")
    return container_water, container_milk, container_coffee


# TODO: 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.

# TODO: 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5


QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNIE = 0.01

water_in_machine = resources["water"]
milk_in_machine = resources["milk"]
coffee_in_machine = resources["coffee"]
money_in_machine = 0

coffee_ordered = coffee_prefer()

if_sufficient_resources = is_resources_sufficient(water_in_machine, milk_in_machine, coffee_in_machine,
                                                  money_in_machine, coffee_ordered)
user_money = process_coins(if_sufficient_resources)
amount_required = MENU[coffee_ordered]["cost"]

print(f"amount required : ${amount_required}\n"
      f"user has given : ${user_money}")
money_in_machine, should_transaction_successful = do_transaction(money_in_machine,)

water_in_machine, milk_in_machine, coffee_in_machine = make_coffee(water_in_machine, milk_in_machine, coffee_in_machine)
