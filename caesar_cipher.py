def caesar_cipher_program():
    text = input("Enter text: ")
    try:
        shift = int(input("Enter shift value: "))
    except ValueError:
        print("Invalid input for shift")
        return
        
    mode = input("Type 'encrypt' or 'decrypt': ").lower()
    
    if mode == 'decrypt':
        shift = -shift
        
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
            
    print(f"Result: {result}")

if __name__ == "__main__":
    caesar_cipher_program()
