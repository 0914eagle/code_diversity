
def solve(n, a, b, k, s):
    # Convert the sequence to a list of integers
    s = [1 if x == '+' else -1 for x in s]
    
    # Initialize the sum to 0
    sum = 0
    
    # Iterate over the sequence
    for i in range(k):
        # Calculate the current term
        term = s[i] * a ** (n - i) * b ** i
        
        # Add the term to the sum
        sum += term
        
        # Take the modulo of the sum
        sum %= 1000000009
    
    # Return the sum
    return sum

