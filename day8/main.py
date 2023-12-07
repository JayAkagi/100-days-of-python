alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

app_running = True

while app_running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    if direction == "exit":
        app_running = False
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))


        def caesar(text, shift):
            secret_message = ""
            for char in text:                   
                if char in alphabet:
                    index = alphabet.index(char)
                    if direction == "encode":
                        new_char = (index + shift) % 26
                    elif direction == "decode":
                        new_char = (index - shift) % 26

                secret_message += alphabet[new_char]
            print(f"The {direction}d text is: {secret_message}")

        caesar(text, shift)

