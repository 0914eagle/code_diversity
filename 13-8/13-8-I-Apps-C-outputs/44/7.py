
def solve(n):
    # Convert n to a binary string
    bin_str = bin(n)[2:]
    
    # Initialize the number of blocked points to 0
    blocked_points = 0
    
    # Iterate through the binary string
    for i in range(len(bin_str)):
        # If the current bit is 1, add 2^i blocked points
        if bin_str[i] == '1':
            blocked_points += 2**i
    
    # Return the minimum number of blocked points
    return blocked_points

