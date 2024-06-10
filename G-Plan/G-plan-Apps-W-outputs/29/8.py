
def calculate_soroban_digit(digit):
    soroban_rep = ""
    if digit == 0:
        soroban_rep = "O-|-OOOO"
    else:
        soroban_rep = "O-|OOOO"
        soroban_rep = soroban_rep[:-(digit % 5)] + "-" + soroban_rep[-(digit % 5):]
    return soroban_rep

def soroban_representation(n):
    n_str = str(n)
    for i in range(len(n_str)-1, -1, -1):
        digit = int(n_str[i])
        print(calculate_soroban_digit(digit))

if __name__ == "__main__":
    n = int(input())
    soroban_representation(n)
