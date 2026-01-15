def investment_growth():
    try:
        amount = float(input("Enter initial investment amount: "))
        rate = float(input("Enter annual interest rate (%): "))
        years = int(input("Enter number of years: "))
    except ValueError:
        print("Invalid input")
        return

    print(f"\n{'Year':<10}{'Amount'}")
    print("-" * 20)
    
    for year in range(1, years + 1):
        amount = amount + (amount * (rate / 100))
        print(f"{year:<10}{amount:.2f}")

if __name__ == "__main__":
    investment_growth()
