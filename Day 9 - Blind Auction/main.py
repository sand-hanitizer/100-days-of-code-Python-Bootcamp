from art import logo
print(logo)
print("Welcome to the Secret Auction!")
more = True
bidders = {}
while(more):
    name = str(input("What is your name? \n"))
    amount = int(input("How much do you bid? \n"))
    bidders[name] = amount
    ask = input("Are there any more people? Y/N \n").upper()
    if ask=='N':
        more = False
    else:
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
max = 0
for key in bidders:
    if bidders[key] > max:
        max = bidders[key]
        name = key
print()
print(f"{name} won the auction with a bid of {max}")
