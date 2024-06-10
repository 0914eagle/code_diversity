
def calculate_digit_representation(digit):
    beads = 'O' + '-' * 4
    rod = '|'
    if digit == 0:
        return f'{beads}{rod}'
    elif digit == 5:
        return f'{rod}{beads}'
    elif digit < 5:
        return f'{beads[:5-digit]}{rod}{beads[5-digit:]}'
    else:
        return f'{rod}{beads[:digit-5]}{beads[digit-5:]}'

def soroban_representation(n):
    digits = [int(d) for d in str(n)]
    for digit in reversed(digits):
        print(calculate_digit_representation(digit))

if __name__ == "__main__":
    n = int(input())
    soroban_representation(n)
