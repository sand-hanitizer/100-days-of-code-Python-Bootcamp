from main import resources
from main import MENU


def info():
    print("Water:", resources["water"], "ml")
    print("Milk", resources["milk"], "ml")
    print("Coffee", resources["coffee"], "grams")
    print(resources["money"], "dollars")


def order(coffee_type):
    flag = 0
    for key in MENU[coffee_type]["ingredients"]:
        if resources[key] < MENU[coffee_type]["ingredients"][key]:
            print(f"Not enough {key}")
            flag = 0
            break
        else:
            flag = 1

    if flag == 1:
        for key in MENU[coffee_type]["ingredients"]:
            resources[key] -= MENU[coffee_type]["ingredients"][key]
        return True
    else:
        return False


def check_money(coffee):
    quarters = int(input("How many quarters do you have?: "))
    dimes = int(input("How many dimes do you have?: "))
    nickels = int(input("How many nickels do you have?: "))
    cents = int(input("How many cents do you have?: "))

    total = quarters*0.25 + dimes*0.10 + nickels*0.05 + cents*0.01
    if MENU[coffee]["cost"] <= total:
        total -= MENU[coffee]["cost"]
        resources["money"] += MENU[coffee]["cost"]
        print("Here's your coffee☕! Your change is {:.2f}".format(total))
    else:
        print("Not enough money! Money refunded")


def refill():
    ask = input("What will you refill?: ")
    resources[ask] += int(input("Amount to refill: "))
