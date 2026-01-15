def calculate_income_tax():
    try:
        income = float(input("Enter your annual taxable income: "))
    except ValueError:
        print("Invalid input")
        return

    tax = 0
    if income <= 250000:
        tax = 0
    elif income <= 500000:
        tax = (income - 250000) * 0.05
    elif income <= 1000000:
        tax = (250000 * 0.05) + (income - 500000) * 0.20
    else:
        tax = (250000 * 0.05) + (500000 * 0.20) + (income - 1000000) * 0.30
        
    print(f"Total Tax Payable: {tax:.2f}")

if __name__ == "__main__":
    calculate_income_tax()
