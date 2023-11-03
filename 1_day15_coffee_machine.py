# TODO 1. MENU AND RECOURCES

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


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# TODO 2. PRINT ALL RESOURCES
print(resources)

# money
profit=0


def resources_sufficient(order_ingredients):
    """Returns True when order can be made False if in insufficient resources"""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            is_enough=False
    return is_enough


def process_coins():
    """Returns the total calculated from coins inserted """
    print("Please insert your coins:")
    total=int(input("how many quarters?: ")) *0.25
    total+=int(input("how many dimes?: ")) *0.1
    total+=int(input("how many nickles?: ")) *0.05
    total+=int(input("how many pennies?: ")) * 0.01
    return total

def transaction_successful(money_received, drink_cost):
    """Returns True when the payment was successful
    otherwise returns False"""
    if drink_cost <= money_received:
        change=round(money_received-drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry there is not enough money. Money refunded.")
        return False

def make_coffe(drink_name,order_ingredients):
    """Makes a coffee and deduct
    the amount of ingredients you have"""
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]

    print(f"Here is your {drink_name} ☕️")

is_on=True
while is_on:
    choice = input("What would you like to drink? (espresso/latte/cappuccino): ")
    if choice=="off":
        is_on=False
    if choice=="report":
        print(f"Water={resources['water']}ml")
        print(f"Milk={resources['milk']}ml")
        print(f"Coffee={resources['coffee']}g")
        print(f"Money=${profit}")

    else:
        drink=MENU[choice]
        print(drink)
        if resources_sufficient(drink["ingredients"]):
            payment= process_coins()
            if transaction_successful(payment,drink["cost"]):
                make_coffe(choice,drink["ingredients"])

















