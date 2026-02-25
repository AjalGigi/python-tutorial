# Q12. Python program to check whether the string is Symmetrical or Palindrome

def is_palindrome(s):
    return s == s[::-1]

def is_symmetrical(s):
    n = len(s)
    if n % 2 != 0:
        return False
    half = n // 2
    return s[:half] == s[half:]

def main():
    string = input("Enter a string: ")

    if is_palindrome(string):
        print(f'"{string}" is a Palindrome')
    else:
        print(f'"{string}" is NOT a Palindrome')

    if is_symmetrical(string):
        print(f'"{string}" is Symmetrical')
    else:
        print(f'"{string}" is NOT Symmetrical')

if __name__ == "__main__":
    main()
