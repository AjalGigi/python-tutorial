# Q14. Rational Number Class with Operator Overloading

from math import gcd

class Rational:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")
        # Handle negative sign
        sign = -1 if (numerator * denominator < 0) else 1
        numerator = abs(numerator)
        denominator = abs(denominator)
        common = gcd(numerator, denominator)
        self.__numerator = sign * (numerator // common)
        self.__denominator = denominator // common

    def getNumerator(self):
        return self.__numerator

    def getDenominator(self):
        return self.__denominator

    def __str__(self):
        if self.__denominator == 1:
            return str(self.__numerator)
        return f"{self.__numerator}/{self.__denominator}"

    def __add__(self, other):
        num = self.__numerator * other.__denominator + other.__numerator * self.__denominator
        den = self.__denominator * other.__denominator
        return Rational(num, den)

    def __sub__(self, other):
        num = self.__numerator * other.__denominator - other.__numerator * self.__denominator
        den = self.__denominator * other.__denominator
        return Rational(num, den)

    def __mul__(self, other):
        num = self.__numerator * other.__numerator
        den = self.__denominator * other.__denominator
        return Rational(num, den)

    def __eq__(self, other):
        return self.__numerator == other.__numerator and self.__denominator == other.__denominator

    def __lt__(self, other):
        return self.__numerator * other.__denominator < other.__numerator * self.__denominator

    def __gt__(self, other):
        return self.__numerator * other.__denominator > other.__numerator * self.__denominator


def main():
    print("=== Rational Number Demo ===")
    r1 = Rational(1, 2)
    r2 = Rational(1, 3)

    print(f"r1 = {r1}")
    print(f"r2 = {r2}")
    print(f"r1 + r2 = {r1 + r2}")
    print(f"r1 - r2 = {r1 - r2}")
    print(f"r1 * r2 = {r1 * r2}")
    print(f"r1 == r2 : {r1 == r2}")
    print(f"r1 < r2  : {r1 < r2}")
    print(f"r1 > r2  : {r1 > r2}")

if __name__ == "__main__":
    main()
