
def calculate_soroban_digit(digit):
    soroban_representation = ""
    if digit >= 5:
        soroban_representation += "O-"
        digit -= 5
    else:
        soroban_representation += "-O"
    soroban_representation += "|"
    soroban_representation += "O" * digit
    soroban_representation += "-"
    soroban_representation += "O" * (4 - digit)
    return soroban_representation

def soroban_representation(n):
    n_str = str(n)
    for i in range(len(n_str)-1, -1, -1):
        digit = int(n_str[i])
        print(calculate_soroban_digit(digit))

if __name__ == "__main__":
    n = int(input())
    soroban_representation(n)
