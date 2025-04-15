

print("Welcome to Caesar Cipher")
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'w', 'z']
encode_decode = input("Type 'encode' to encript, type 'decode to decrypt:\n".lower())
text = input("Type your message:\n".lower())
shift = int(input("Type the shift number:\n"))

def caesar(original_text, shift_amount):
    output_text = ""
    for letter  in original_text:
        if encode_decode == "encode":
            shifted_position=alphabet.index(letter) + shift_amount
        elif encode_decode == "decode":
            shifted_position = alphabet.index(letter) - shift_amount
        else:
            print ("Please choose one of the options suggested")
        shifted_position %= len(alphabet)#this line of code guards against letters beyond the end of the alphabet
        output_text += alphabet[shifted_position]

    print (f"Here is the encoded result : {output_text}")

caesar(original_text = text, shift_amount=shift)
    #return new_letter


