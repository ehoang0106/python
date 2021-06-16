from file import alphabet



def cipher(start_text, shift_amount, dictionary):
    if dictionary == "decode":
        shift_amount *= -1

    end_text = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Your {dictionary} is {end_text}")

continue_cipher = True
while continue_cipher:
    dic = input("Type encode to encrypt or type decode to decrypt: ").lower()
    text = input("Type your text: ").lower()
    shift = int(input("Type shift amount: "))
    shift = shift % 26
    cipher(start_text=text, shift_amount=shift, dictionary=dic)


    cont = input("Do you want to continue? Type Y or N\n").lower()
    if cont == "n":
        continue_cipher = False
        print("Goodbye!")


# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         cipher_text  += alphabet[new_position]
#     print(f"Your {dic} is {cipher_text}")
#
# def decrypt(cipher_text, shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
#     print(f"Your {dic} is {plain_text}")
#
# if dic == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif dic == "decode":
#     decrypt(cipher_text=text, shift_amount=shift)