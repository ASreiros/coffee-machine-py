from functions import report, turn_off, teapod, make_coffee, fill
from art import logo


print(logo)
work = True
while work:
    command_flag = False
    while not command_flag:
        command_flag = True
        user_choice = input("What would you like? (espresso, latte, cappuccino):   ")

        if user_choice == 'report':
            report()
        elif user_choice == 'off':
            work = turn_off()
        elif user_choice == '418':
            work = teapod()
        elif user_choice == 'fill':
            fill()
        elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
            make_coffee(user_choice)
        else:
            print("Sorry, that is not a correct command. Here is the list of the correct commands:")
            print("espresso, latte, cappuccino, report, fill, off, 418")
            command_flag = False
