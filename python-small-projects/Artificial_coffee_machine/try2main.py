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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can ve made, False if ingredients are insufficient"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            is_enough = False
    return is_enough


def process_coins():
    """Returns the total calculated from coins inserted."""
    print('please insert coins. ')
    total = int(input("how many quarters? : ")) * 0.25
    total += int(input("how many dimes? : ")) * 0.1
    total += int(input("how many nickles? : ")) * 0.05
    total += int(input("how many pennies? : ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted or False if money is insufficient."""
    print(f" drink_cost is {drink_cost}")
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is ${change} change for money received ")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients form the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕︎ ")


should_true = True
while should_true:
    choice = input(f"What would you like ? (espresso/latte/cappuccino) :")
    if choice == "off":
        should_true = False
    elif choice == "report":
        print(f"water : {resources["water"]}ml")
        print(f"milk : {resources["milk"]}ml")
        print(f"coffee : {resources["coffee"]}g")
        print(f"money : ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
