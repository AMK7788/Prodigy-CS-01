def caesar_cipher_encrypt(plain_text, shift):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():  # Check if the character is an alphabet
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(encrypted_text, shift):
    return caesar_cipher_encrypt(encrypted_text, -shift)

def main():
    while True:
        choice = input("Enter 'e' for encryption, 'd' for decryption, or 'q' to quit: ")
        if choice == 'e':
            plain_text = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_text = caesar_cipher_encrypt(plain_text, shift)
            print("Encrypted text:", encrypted_text)
        elif choice == 'd':
            encrypted_text = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_text = caesar_cipher_decrypt(encrypted_text, shift)
            print("Decrypted text:", decrypted_text)
        elif choice == 'q':
            print("Exiting the programm. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'e' for encryption, 'd' for decryption, or 'q' to quit.")

if __name__ == "__main__":
    main()
