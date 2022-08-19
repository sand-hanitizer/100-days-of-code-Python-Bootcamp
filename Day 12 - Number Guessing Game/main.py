from random import randint
logo = """ 
   _____                       _   _            _   _                 _               _ 
  / ____|                     | | | |          | \ | |               | |             | |
 | |  __ _   _  ___  ___ ___  | |_| |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __| |
 | | |_ | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__| |
 | |__| | |_| |  __/\__ \__ \ | |_| | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |  |_|
  \_____|\__,_|\___||___/___/  \__|_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|  (_)
                                                                                        
                                                                                        
"""
print(logo)


def game():
    number = randint(1,100)
    print("I'm thinking of a number between 1 and 100")
    level = input("How would you like to play this game? Easy/Hard: ").lower()
    if level == "easy":
        attempts = 10
    elif level == "hard":
        attempts = 5
    else:
        print("Invalid Input")
        attempts = 0

    while(attempts > 0):
        a = int(input("Enter what number you think it is: "))
        if a == number:
            print(f"You got it! {a} was the correct answer")
            break
        else:
            if a > number:
                print("Too high!")
            elif a < number:
                print("Too low!")
            attempts -= 1
            print(f"You have {attempts} chances left.")
    
    if attempts == 0: print("You lost!")


game()
ask = input("Do you want to go again? Y/N").upper()
if ask=='Y':
    game()
else:
    print("Goodbye!")

