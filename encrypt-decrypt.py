from art import logo
from a import alphabet

print(logo)

def extend_alphabet(text,shift):
    last_letters = {'v','w','x','y','z'}
    if any(letter in last_letters for letter in text):
        alphabet.extend(alphabet)

def encrypt(text, shift):
    encrypted_text = ""
    for letters in text:
        if letters in alphabet:
            position = alphabet.index(letters)+shift
            encrypted_text += alphabet[position]
        else:
            encrypted_text += letters
    print(f"The encoded text is {encrypted_text}")

def decrypt(text, shift):
    decrypted_text = ""
    for letters in text:
        if letters in alphabet:
            position = alphabet.index(letters)-shift
            decrypted_text+=alphabet[position]
        else:
            decrypted_text+=letters
    print(f"The decoded text is {decrypted_text}")

close_program = False
while not close_program:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    extend_alphabet(text, shift)
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)

    restart = input("Type 'yes' to want to go again, type 'no' to want to quit. \n").lower()
    if restart == "no":
        close_program= True
        print("Thanks for using Caesar Cipher!")
