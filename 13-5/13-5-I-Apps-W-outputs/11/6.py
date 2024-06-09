
def is_human_winner(coefficients, k):
    # Initialize the polynomial with the given coefficients
    polynomial = 0
    for i, coefficient in enumerate(coefficients):
        if coefficient != '?':
            polynomial += int(coefficient) * x ** i

    # Check if the polynomial is already divisible by x - k
    if polynomial % (x - k) == 0:
        return True

    # Check if the human can set a coefficient to any value and still win
    for i in range(len(coefficients)):
        if coefficients[i] == '?':
            # Set the coefficient to any value and check if the polynomial is still divisible by x - k
            coefficients[i] = 1
            polynomial += 1 * x ** i
            if polynomial % (x - k) == 0:
                return True
            # Reset the coefficient to ? and try the next one
            coefficients[i] = '?'

    # If the human cannot set a coefficient to any value and still win, return False
    return False

def main():
    n, k = map(int, input().split())
    coefficients = [input() for _ in range(n + 1)]
    print("Yes") if is_human_winner(coefficients, k) else print("No")

if __name__ == '__main__':
    main()

