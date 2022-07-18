from random import choice


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
user_input = int(input())
choices = [rock,paper,scissors]
names = ["Rock","Paper","Scissors"]
user_choice = choices[user_input]
print(f"You chose {names[user_input]}")
print(user_choice)
comp_choice = choice([0,1,2])
print(f"The computer chose {names[comp_choice]}")
print(choices[comp_choice])
if user_input == comp_choice:
    print("A tie")
else:
    if(comp_choice - user_input == 1):
        print("You Lose")
    else:
        print("You Win!")
