def caesar_cipher_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shifted_char = chr((ord(char) - shift - 65) % 26 + 65) if char.isupper() else chr((ord(char) - shift - 97) % 26 + 97)
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text

# Get user input for encryption
encrypted_message = input("Enter the message to decrypt: ")
shift = int(input("Enter the shift value: "))

# Decrypt the message using Caesar cipher
decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
print("Decrypted message:", decrypted_message)