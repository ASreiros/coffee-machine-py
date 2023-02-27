from machine_data import resources, MENU


def report():
    """Makes report about resources"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    money = resources.get("money", 0)
    print(f"Money: ${money}")


def turn_off():
    """Turns off coffee machine"""
    print("Coffee machine now will be turned off")
    return False


def teapod():
    """Makes joke and turns off coffee machine"""
    print("I can't make coffee because I'm a teapot")
    return turn_off()


def fill():
    for res in resources:
        flag = False
        while not flag:
            add = input(f"Please enter how much {'gr' if res == 'coffee' else 'ml' } of {res} you want to add:  ")
            if add.isdigit():
                resources[res] += int(add)
                flag = True
            else:
                print("That is not a valid number.")
def pour_coffee(coffee):
    """Pours coffee. Adjust resources. End step"""
    bank = resources.get("money", 0)
    resources["money"] = round(bank + MENU[coffee]["cost"], 2)
    for res in resources:
        resources[res] -= MENU[coffee]["ingredients"].get(res, 0)

    print(f"Here is your {coffee}. Enjoy!")


def payment_evaluator(coffee, total):
    """Evaluates payment. If payment is enough starts next step. Otherwise warn user."""
    if MENU[coffee]["cost"] == total:
        pour_coffee(coffee)
    elif MENU[coffee]["cost"] < total:
        print(f"Here is ${round(total - MENU[coffee]['cost'], 2)} in change.")
        pour_coffee(coffee)
    else:
        print(f"Sorry, that's not enough money. You have only ${total}. Price is ${MENU[coffee]['cost']}.")
        if input("Do you want to add coins? Type 'y' or 'n' for no:  ").lower() == "y":
            payment(coffee, total)
        else:
            print(f"Money refunded in amount ${total}")


def payment(coffee, already_paid):
    """Accepts coins and calls next function"""
    coins = {
        "pennies": 0,
        "nickels": 0,
        "dimes": 0,
        "quarters": 0
    }
    for coin in coins:
        payment_flag = False
        while not payment_flag:
            nr_of_coins = input(f"Please enter how many {coin} do you want to pay?")
            if nr_of_coins.isdigit():
                payment_flag = True
                coins[coin] = int(nr_of_coins)
            else:
                print("Please enter valid number")

    total = already_paid + (coins["pennies"] + coins["nickels"]*5 + coins["dimes"]*10 + coins["quarters"]*25)/100
    total = round(total, 2)
    print(f"Total paid amount is ${total}")
    payment_evaluator(coffee, total)


def make_coffee(coffee):
    """Checks if there are resources and moves to next step or warn user that resources insufficient"""
    res_flag = True
    for res in resources:
        if MENU[coffee]["ingredients"].get(res, 0) > resources[res]:
            print(f"Sorry there is not enough {res}.")
            res_flag = False

    if res_flag:
        payment(coffee, 0)
