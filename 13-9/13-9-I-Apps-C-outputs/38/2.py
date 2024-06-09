
def count_ways(N, d):
    # Initialize the result
    result = 1
    
    # Iterate over each part
    for i in range(N):
        # Calculate the number of ways to connect the current part to the previous parts
        num_ways = 1
        for j in range(i):
            num_ways *= d[j]
        
        # Add the number of ways to connect the current part to the result
        result += num_ways
    
    # Return the result modulo 998244353
    return result % 998244353

