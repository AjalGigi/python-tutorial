def square_root_custom():
    try:
        number = float(input("Enter a number: "))
    except ValueError:
        print("Invalid input")
        return

    if number < 0:
        print("Cannot calculate square root of negative number")
        return
        
    tolerance = 1e-10
    guess = number / 2.0
    while True:
        new_guess = (guess + number / guess) / 2.0
        if abs(new_guess - guess) < tolerance:
            break
        guess = new_guess
        
    print(f"Square root of {number} is approximately {guess}")

if __name__ == "__main__":
    square_root_custom()
