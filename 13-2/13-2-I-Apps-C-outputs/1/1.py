
def solve(n, a, b, k, s):
    # Convert the sequence to a list of integers
    s = [1 if x == '+' else -1 for x in s]
    
    # Initialize the result
    result = 0
    
    # Iterate over the period of the sequence
    for i in range(k):
        # Calculate the current term
        term = s[i] * a ** (n - i) * b ** i
        
        # Add the term to the result
        result = (result + term) % (10 ** 9 + 9)
    
    # Return the result
    return result

