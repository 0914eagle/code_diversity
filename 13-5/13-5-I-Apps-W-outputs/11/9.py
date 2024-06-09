
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
            # Set the coefficient to any value and check if the resulting polynomial is divisible by x - k
            coefficients[i] = 1
            polynomial = 0
            for j in range(n):
                polynomial += coefficients[j] * x**j
            if polynomial % (x - k) == 0:
                return True
    
    # Check if the human can set a coefficient to 0 and win
    for i in range(n):
        if coefficients[i] == '?':
            # Set the coefficient to 0 and check if the resulting polynomial is divisible by x - k
            coefficients[i] = 0
            polynomial = 0
            for j in range(n):
                polynomial += coefficients[j] * x**j
            if polynomial % (x - k) == 0:
                return True
    
    # If none of the above conditions are met, the human cannot win
    return False

def main():
    n, k = map(int, input().split())
    coefficients = []
    for i in range(n + 1):
        coefficient = input()
        if coefficient == '?':
            coefficients.append('?')
        else:
            coefficients.append(int(coefficient))
    print("Yes") if is_human_winner(n, k, coefficients) else print("No")

if __name__ == '__main__':
    main()

