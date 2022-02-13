# Python script for caesar cipher

import cipher_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(cipher_art.logo)

direction = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("\nType your message:\n").lower()
shift = int(input("\nType the shift number:\n"))

def encrypt(text, shift):
    msg = ""
    for index in range(len(text)):
        current_letter = text[index]
        new_letter_index = (alphabet.index(current_letter) + shift) % 26
        new_letter = alphabet[new_letter_index]
        msg += new_letter
    print(f"\nYour encrypted message is: {msg}\n")

def decrypt(text, shift):
    msg = ""
    for index in range(len(text)):
        current_letter = text[index]
        new_letter_index = (alphabet.index(current_letter) - shift) % 26
        new_letter = alphabet[new_letter_index]
        msg += new_letter
    print(f"\nYour decrypted message is: {msg}\n")


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Please type encode or decode. Try again.")