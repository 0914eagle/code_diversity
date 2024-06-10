
def calculate_soroban_representation(n):
    soroban_digits = []
    while n > 0:
        digit = n % 10
        soroban_digits.append(digit)
        n //= 10
    return soroban_digits

def print_soroban_representation(digit):
    soroban = ""
    soroban += "O-" if digit >= 5 else "O"
    soroban += "|"
    soroban += "-" * (4 - digit % 5) if digit % 5 != 0 else ""
    return soroban

def print_soroban(n):
    soroban_digits = calculate_soroban_representation(n)
    for digit in soroban_digits[::-1]:
        print(print_soroban_representation(digit))

if __name__ == "__main__":
    n = int(input())
    print_soroban(n)
