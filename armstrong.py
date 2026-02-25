def check_armstrong():
    try:
        num = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input")
        return
        
    # Change num to string to calculate length (order)
    order = len(str(num))
    
    sum_val = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_val += digit ** order
        temp //= 10

    if num == sum_val:
        print(f"{num} is an Armstrong number")
    else:
        print(f"{num} is not an Armstrong number")

if __name__ == "__main__":
    check_armstrong()
