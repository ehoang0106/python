from file import alphabet,number
#create function cipher
def cipher(start_text, shift_amount, dictionary):
    if choice == "decode":
        shift_amount *= -1

    encoded = ""
    #
    for char in start_text:
        if char in alphabet:
            position =  alphabet.index(char)
            new_position = position + shift_amount
            encoded += alphabet[new_position]
        elif char in number:
            position = number.index(char)
            new_position = position + shift_amount
            encoded += number[new_position]
        else:
            encoded += char
    print(f"{text.upper()} after {choice} is {encoded.upper()} ")



stop_encode = False

while not stop_encode:
    choice = input("Type 'encode' to encrypt or 'decode' to decrypt: \n")
    text = input("Input message: \n")
    shift = int(input("Shift amount: \n"))
    shift = shift % 26
    cipher(start_text=text, shift_amount=shift, dictionary=choice)

    #
    result = input("Do you want to continue? Type 'y' or 'n'\n").lower()
    if result == "n":
        stop_encode = True
        print("Goodbye! hihi")


















