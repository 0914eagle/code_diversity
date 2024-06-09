
def is_human_winner(n, k, coefficients):
    # Initialize the polynomial with the given coefficients
    polynomial = 0
    for i in range(n):
        polynomial += coefficients[i] * x**i

    # Check if the polynomial is already divisible by x - k
    if polynomial % (x - k) == 0:
        return True

    # Check if the human can set a coefficient to any value and win
    for i in range(n):
        if coefficients[i] == '?':
            # Set the coefficient to any value and check if the polynomial is divisible by x - k
            coefficients[i] = 1
            if polynomial % (x - k) == 0:
                return True
            coefficients[i] = -1
            if polynomial % (x - k) == 0:
                return True
            coefficients[i] = 0
            if polynomial % (x - k) == 0:
                return True
            coefficients[i] = '?'

    # If the human cannot set a coefficient to any value and win, return False
    return False

def main():
    n, k = map(int, input().split())
    coefficients = [int(input()) for _ in range(n + 1)]
    print("Yes") if is_human_winner(n, k, coefficients) else print("No")

if __name__ == '__main__':
    main()

