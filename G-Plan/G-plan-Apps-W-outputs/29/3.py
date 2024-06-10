
def calculate_digit_representation(digit):
    beads = 'O' + '-' * (4 - digit)
    return beads

def soroban_representation(n):
    digits = [int(d) for d in str(n)]
    for i in range(len(digits) - 1, -1, -1):
        beads = calculate_digit_representation(digits[i])
        rod = beads + '|' + '-' * i
        print(rod)

if __name__ == "__main__":
    n = int(input())
    soroban_representation(n)
