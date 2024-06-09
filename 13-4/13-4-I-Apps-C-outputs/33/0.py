
def solve(n, a, b, k, s):
    # Convert the sequence to a list of integers
    s = [1 if x == '+' else -1 for x in s]
    
    # Initialize the sum to 0
    sum = 0
    
    # Iterate over the indices 0 to n
    for i in range(n):
        # Calculate the value of a^i and b^i
        ai = a ** (n - i)
        bi = b ** i
        
        # Add the current term to the sum
        sum += s[i % k] * ai * bi
    
    # Return the sum modulo 10^9 + 9
    return sum % (10**9 + 9)

