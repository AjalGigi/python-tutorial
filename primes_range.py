def primes_in_range():
    try:
        lower = int(input("Enter lower bound (m): "))
        upper = int(input("Enter upper bound (n): "))
    except ValueError:
        print("Invalid input")
        return

    print(f"Prime numbers between {lower} and {upper} are:")
    for num in range(lower, upper + 1):
        if num > 1:
            for i in range(2, int(num**0.5) + 1):
                if (num % i) == 0:
                    break
            else:
                print(num)

if __name__ == "__main__":
    primes_in_range()
