def string_operations_program():
    # Create
    str1 = input("Enter first string: ")
    str2 = input("Enter second string: ")
    
    # Concatenate
    concat_str = str1 + str2
    print(f"Concatenated: {concat_str}")
    
    # Substring (first 3 chars)
    if len(concat_str) >= 3:
        print(f"First 3 chars: {concat_str[:3]}")
        
    # Reverse
    reverse_str = concat_str[::-1]
    print(f"Reversed: {reverse_str}")
    
    # Palindrome Check
    is_palindrome = (concat_str == reverse_str)
    if is_palindrome:
        print("The concatenated string is a Palindrome")
    else:
        print("The concatenated string is Symmetrical but NOT a Palindrome" if len(str1)==len(str2) else "Not a Palindrome")

if __name__ == "__main__":
    string_operations_program()
