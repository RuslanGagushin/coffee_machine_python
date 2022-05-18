# Coffee machine project

# Menu of the coffee machine
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

# profit
profit = 0.0

# resources of the coffee machine
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Check resources before make a coffee"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry it's not enough {item}")
            return False
    return True


def process_coins():
    """Return total coins insert"""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True if money is enough for make a coffee"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        global profit
        profit += drink_cost
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}")


def refill():
    """Refill resources"""
    global profit
    global resources
    profit = 0.0
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }


work_on = True  # Turn on the coffee machine

while work_on:
    customer_choise = input("What would you like? (espresso/latte/cappuccino):")
    if customer_choise == "off":
        work_on = False
        print("Coffee machine turned off, have a nice day!")
    elif customer_choise == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: $ {profit}")
    elif customer_choise == "refill":
        refill()
        print("refill is completed!")
    else:
        # Take a drink from menu
        drink = MENU[customer_choise]
        # Check resources for make a coffee
        if is_resource_sufficient(drink["ingredients"]):
            # Calculate the payment
            payment = process_coins()
            # Check enough money
            if is_transaction_successful(payment, drink["cost"]):
                # Make a coffee!
                make_coffee(customer_choise, drink["ingredients"])
