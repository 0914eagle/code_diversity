
def calculate_soroban_digit(digit):
    if digit == 0:
        return "O-|-OOOO"
    elif digit == 1:
        return "O-|OOOO-"
    elif digit == 2:
        return "O-|OOO-O"
    elif digit == 3:
        return "O-|OO-OO"
    elif digit == 4:
        return "O-|O-OOO"
    elif digit == 5:
        return "O-|O-OO-"
    elif digit == 6:
        return "O-|O--OO"
    elif digit == 7:
        return "O-|-OOOO"
    elif digit == 8:
        return "O-|-OOO-"
    elif digit == 9:
        return "O-|-O-OO"

def soroban_representation(n):
    digits = [int(d) for d in str(n)]
    for digit in reversed(digits):
        print(calculate_soroban_digit(digit))

if __name__ == "__main__":
    n = int(input())
    soroban_representation(n)
