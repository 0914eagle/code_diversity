
def is_human_winner(n, k, coefficients):
    # Initialize the polynomial and the remaining undefined coefficients
    polynomial = 0
    undefined_coefficients = set(range(1, n + 1))

    # Iterate through the given coefficients
    for i, coefficient in enumerate(coefficients, start=1):
        # If the coefficient is undefined, add it to the polynomial and remove it from the set of undefined coefficients
        if coefficient == '?':
            polynomial += f"x^{i}"
            undefined_coefficients.remove(i)
        # If the coefficient is defined, add it to the polynomial
        else:
            polynomial += f"{coefficient}x^{i}"

    # Check if the resulting polynomial is divisible by x - k
    if polynomial % f"x - {k}" == 0:
        return True

    # If the polynomial is not divisible by x - k, check if the human can set an undefined coefficient to any value and win
    for i in undefined_coefficients:
        # Set the coefficient to any value and check if the resulting polynomial is divisible by x - k
        polynomial = polynomial.replace(f"x^{i}", f"{i}x^{i}")
        if polynomial % f"x - {k}" == 0:
            return True

    # If the human cannot set any undefined coefficient to any value and win, return False
    return False

def main():
    n, k = map(int, input().split())
    coefficients = input().split()
    print("Yes") if is_human_winner(n, k, coefficients) else print("No")

if __name__ == '__main__':
    main()

