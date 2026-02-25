def fibonacci_sequence():
    try:
        nterms = int(input("How many terms? "))
    except ValueError:
        print("Invalid input")
        return

    n1, n2 = 0, 1
    count = 0

    if nterms <= 0:
        print("Please enter a positive integer")
    elif nterms == 1:
        print(f"Fibonacci sequence upto {nterms}:")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1)
            nth = n1 + n2
            # update values
            n1 = n2
            n2 = nth
            count += 1

if __name__ == "__main__":
    fibonacci_sequence()
