# Q11. Program to Reverse a String

def reverse_string(s):
    return s[::-1]

def main():
    string = input("Enter a string: ")
    reversed_str = reverse_string(string)
    print(f"Original String : {string}")
    print(f"Reversed String : {reversed_str}")

if __name__ == "__main__":
    main()
