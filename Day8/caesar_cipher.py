

print("Welcome to Caesar Cipher")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'w', 'z']
direction = input("Type 'encode' to encript, type 'decode to decrypt:\n".lower())
text = input("Type your message:\n".lower())
shift = int(input("Type the shift number:\n"))



def encrypt(original_text, shift_amount):
    cipher_text = ""

    for letter  in original_text:
        shifted_position=alphabet.index(letter) + shift_amount

        shifted_position %= len(alphabet)#this line of code guards against letters beyond the end of the alphabet
        cipher_text += alphabet[shifted_position]

    print (f"Here is the encoded result : {cipher_text}")

encrypt(original_text = text, shift_amount=shift)
    #return new_letter

#encrypt ('hello', 1)