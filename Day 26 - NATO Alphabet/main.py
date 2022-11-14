import pandas as pd

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pd.read_csv("nato_phonetic_alphabet.csv")
# TODO 1. Create a dictionary in this format:
nato_dict = {row.letter: row.code for (index, row) in data.iterrows()}
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.


def output():
    name = list(input("Enter your name: ").upper())
    try:
        list_name = [nato_dict[x] for x in name]
    except KeyError:
        print("Sorry, only letters are accepted.")
        output()
    else:
        print(list_name)


output()
