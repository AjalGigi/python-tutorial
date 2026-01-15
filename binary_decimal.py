def binary_to_decimal_program():
    binary_str = input("Enter binary string: ")
    try:
        decimal = 0
        power = 0
        for digit in reversed(binary_str):
            if digit == '1':
                decimal += 2 ** power
            elif digit != '0':
                print("Invalid binary string")
                return
            power += 1
        print(f"Decimal value: {decimal}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    binary_to_decimal_program()
