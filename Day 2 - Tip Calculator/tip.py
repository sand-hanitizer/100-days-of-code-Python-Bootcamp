print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? Rs."))
num = int(input("How many people are splitting the bill? "))
tip = int(input("What percentage tip would you like to give? 5,10 or 15? "))
if tip==5:
    total = bill + 0.05*bill
elif tip == 10:
    total = bill + 0.1*bill
elif tip==15:
    total = bill + 0.15*bill
else:
    print("Invalid tip amount")
final = total / num
print("Each person should pay Rs. {0:.2f}".format(final))