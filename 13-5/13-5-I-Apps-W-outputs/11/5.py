
def is_human_winner(n, k, coefficients):
    # Initialize the polynomial and the remaining undefined coefficients
    polynomial = 0
    undefined_coefficients = set(range(1, n + 1))

    # Iterate through the coefficients and set the undefined coefficients
    for i, coefficient in enumerate(coefficients, start=1):
        if coefficient != "?":
            polynomial += int(coefficient) * x**(i - 1)
            undefined_coefficients.remove(i)

    # Check if the polynomial is divisible by x - k
    if polynomial % (x - k) == 0:
        return True

    # Check if the human can set an undefined coefficient to make the polynomial divisible by x - k
    for i in undefined_coefficients:
        polynomial += x**(i - 1)
        if polynomial % (x - k) == 0:
            return True
        polynomial -= x**(i - 1)

    return False

def main():
    n, k = map(int, input().split())
    coefficients = input().split()
    print("Yes") if is_human_winner(n, k, coefficients) else print("No")

if __name__ == '__main__':
    main()

