# ceaser's encoding 
from files.caesar_cipher.alphabet import alphabet

choice = input("Type 'encode' to encrpyt, type 'decode' to decrpyt: \n")
message = input("Type your message:\n").lower()
shift = int(input("Type the shift number: \n"))     

def encrpyt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"The decoded text is {plain_text}")    
    
    
if choice == "encode":
    encrpyt(plain_text=message, shift_amount=shift)
elif choice == "decode":
    decrypt(cipher_text=message, shift_amount=shift)

