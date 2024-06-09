
def solve(n, a, b, k, s):
    # Convert the sequence to a list of integers
    s = [1 if x == '+' else -1 for x in s]
    
    # Initialize the sum to 0
    sum = 0
    
    # Iterate over the sequence
    for i in range(k):
        # Calculate the current term
        term = s[i] * a**(n-i) * b**i
        
        # Add the term to the sum
        sum += term
        
        # If the sum exceeds 10^9 + 9, subtract 10^9 + 9 to keep it within the modulo
        if sum > 10**9 + 9:
            sum -= 10**9 + 9
    
    # Return the sum modulo 10^9 + 9
    return sum % (10**9 + 9)

