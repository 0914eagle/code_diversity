
def calculate_soroban_digit(digit):
    soroban_representation = ""
    if digit == 0:
        soroban_representation = "O-|-OOOO"
    else:
        go_dama = "O" if digit >= 5 else "-"
        ichi_damas = "O" * (digit % 5) + "-" * (5 - digit % 5)
        soroban_representation = f"{go_dama}|{ichi_damas}"
    return soroban_representation

def soroban_representation(n):
    digits = [int(d) for d in str(n)]
    for digit in reversed(digits):
        print(calculate_soroban_digit(digit))

if __name__ == "__main__":
    n = int(input())
    soroban_representation(n)