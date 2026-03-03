# Name: Ivy Loi
# Assignment: HW 1
# Problem: 1b
# Date: 3/2/26
# Do long division and return the quotient and remainder
def long_division(num, denom):
    if denom == 0:
        raise ValueError("Denominator cannot be zero.")
    
    quotient = num // denom
    remainder = num % denom
    
    return quotient, remainder

def main():
    num = 10
    denom = 3
    quotient, remainder = long_division(num, denom)
    print(f"Quotient: {quotient}, Remainder: {remainder}")

main()