
def is_human_winner(n, k, coefficients):
    # Initialize the polynomial as a string
    polynomial = "".join(str(c) for c in coefficients)
    
    # Check if the polynomial is already divisible by x - k
    if polynomial.endswith(f"x - {k}"):
        return True
    
    # Check if the polynomial has any undefined coefficients
    if "?" in polynomial:
        return False
    
    # Check if the polynomial is divisible by x - k after setting the last coefficient to any value
    for i in range(n):
        polynomial = polynomial[:-1] + str(i)
        if polynomial.endswith(f"x - {k}"):
            return True
    
    # If none of the above conditions are met, the human has no winning strategy
    return False

def main():
    n, k = map(int, input().split())
    coefficients = list(map(int, input().split()))
    print("Yes") if is_human_winner(n, k, coefficients) else print("No")

if __name__ == '__main__':
    main()

