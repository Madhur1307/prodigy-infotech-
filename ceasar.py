


def caesar_cipher_encrypt(message, shift):
    encrypted_message = ""  
    for char in message:
        if char.isalpha():  
            shift_base = ord('A') if char.isupper() else ord('a') 
            
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char  
    return encrypted_message


def caesar_cipher_decrypt(message, shift):
    
    return caesar_cipher_encrypt(message, -shift)

def main():
    while True:
        
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? (Enter 'exit' to quit): ").lower()
        if choice == 'e':
            
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted message: {encrypted_message}")
        elif choice == 'd':
            
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print(f"Decrypted message: {decrypted_message}")
        elif choice == 'exit':
            break  
        else:
            print("Invalid choice. Please enter 'e' to encrypt, 'd' to decrypt, or 'exit' to quit.")


if __name__ == "__main__":
    main()
