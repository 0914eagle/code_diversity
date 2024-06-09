
def is_human_winnable(n, k, coefficients):
    # Initialize the polynomial with the given coefficients
    polynomial = 0
    for i in range(n):
        polynomial += coefficients[i] * x**i
    
    # Check if the polynomial is already divisible by x - k
    if polynomial % (x - k) == 0:
        return True
    
    # Check if the human can set the coefficient of the highest power to any value and still win
    if coefficients[-1] == 0:
        return True
    
    # Check if the human can set the coefficient of the second highest power to any value and still win
    if coefficients[-2] == 0:
        return True
    
    # Check if the human can set the coefficient of the third highest power to any value and still win
    if coefficients[-3] == 0:
        return True
    
    # If none of the above conditions are met, the human cannot win
    return False

def main():
    n, k = map(int, input().split())
    coefficients = list(map(int, input().split()))
    print("Yes") if is_human_winnable(n, k, coefficients) else print("No")

if __name__ == '__main__':
    main()

