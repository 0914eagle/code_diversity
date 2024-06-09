
def is_winning_strategy(polynomial, k):
    # Check if the polynomial is already divisible by x - k
    if polynomial % (x - k) == 0:
        return True
    
    # Check if the polynomial has any undefined coefficients
    if any(coeff == '?' for coeff in polynomial):
        return False
    
    # Check if the polynomial has any negative coefficients
    if any(coeff < 0 for coeff in polynomial):
        return False
    
    # Check if the polynomial has any coefficient equal to 0
    if any(coeff == 0 for coeff in polynomial):
        return False
    
    # Check if the polynomial has any coefficient greater than 1
    if any(coeff > 1 for coeff in polynomial):
        return False
    
    # If all the above conditions are not met, then the human has a winning strategy
    return True

def main():
    polynomial, k = map(int, input().split())
    polynomial = [int(input()) for _ in range(polynomial)]
    print("Yes") if is_winning_strategy(polynomial, k) else print("No")

if __name__ == '__main__':
    main()

