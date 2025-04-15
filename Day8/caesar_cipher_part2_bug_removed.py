
print("Welcome to Caesar Cipher")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'w', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n".lower())
text = input("Type your message:\n".lower())
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift_amount, encode_decode):
    output_text = ""

    if encode_decode == "decode":
        shift_amount *= -1

    for letter in original_text:

        shifted_position=alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]

    print (f"Here is the {encode_decode}d result : {output_text}")

caesar(original_text = text, shift_amount=shift, encode_decode=direction)
    #return new_letter


