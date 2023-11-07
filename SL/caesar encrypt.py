def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97)
            encrypted_text += shifted_char
        else:
            encrypted_text += char
    return encrypted_text

# Get user input for encryption
message = input("Enter the message to encrypt: ")
shift = int(input("Enter the shift value: "))

# Encrypt the message using Caesar cipher
encrypted_message = caesar_cipher_encrypt(message, shift)
print("Encrypted message:", encrypted_message)