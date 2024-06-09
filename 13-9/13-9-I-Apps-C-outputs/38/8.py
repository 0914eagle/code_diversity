
def solve(N, d):
    # Calculate the number of ways to connect the parts
    num_ways = 1
    for i in range(N):
        num_ways *= d[i]
    
    # Calculate the number of connected components
    num_connected = N - 1
    
    # Calculate the number of ways to connect the parts with connecting components
    for i in range(N):
        for j in range(i+1, N):
            num_ways -= d[i] * d[j]
    
    # Calculate the number of ways to connect the parts with connecting components and the number of connected components
    num_ways //= num_connected
    
    # Return the result modulo 998244353
    return num_ways % 998244353

