# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
with open("Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

f_list = []
for name in names_list:
    x = name.strip('\n')
    f_list.append(x)


# Replace the [name] placeholder with the actual name.
with open("Input/Letters/starting_letter.txt","r") as letter:
    content = letter.read()

# Save the letters in the folder "ReadyToSend".
for name in f_list:
    with open(f"Output/ReadyToSend/letter_to_{name}","w") as file:
        letter = content
        letter = letter.replace("[name]",f"{name}")
        file.write(letter)
