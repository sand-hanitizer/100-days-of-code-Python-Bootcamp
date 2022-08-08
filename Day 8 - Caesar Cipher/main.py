from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text,shift,direction):
  l = list(text)
  ans = ''
  shift = shift%26
  if direction == "decode":
    shift *= -1
  for a in l:
    if a in alphabet:
      i = alphabet.index(a)
      if i+shift < 26:
          ans = ans + alphabet[i+shift]
      else:
          ans = ans + alphabet[shift - i - 2]
    else:
      ans += a
  print(f"The {direction}d text is {ans}")
  
cont = True
while(cont == True):
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  caesar(text=text,shift=shift,direction=direction)
  ask = input("Do you wish to continue? Type 'yes' or 'no'\n").lower()
  if ask =="no":
      cont = False
      print("Goodbye!")
