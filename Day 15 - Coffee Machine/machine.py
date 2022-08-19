import actions

on = True
while on:
    quest = input("What kind of coffee will you have today?(espresso/latte/cappuccino): ")
    if quest == "off":
        on = False
    elif quest == "report":
        actions.info()
    elif quest == "refill":
        actions.refill()
    else:
        if actions.order(quest):
            actions.check_money(quest)
