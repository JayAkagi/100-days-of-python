alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            encrypted_index = (index + shift) % 26
            encrypted_char = alphabet[encrypted_index]
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

encrypted_text = encrypt(text,shift)

def decrypt(text, shift):
    decrypted_text =""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            decrypt_index = (index - shift) % 26
            decrypted_char = alphabet[decrypt_index]
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text

decrypted_text = decrypt(text, shift)

if direction == "encode":
    encrypt(text, shift)
    print(encrypted_text)
elif direction == "decode":
    decrypt(text, shift)
    print(decrypted_text)
else:
    print("Invalid option.")