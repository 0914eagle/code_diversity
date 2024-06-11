def solve(N):
    
    # Convert N to binary
    binary = bin(N)[2:]
    # Convert binary to integer
    binary = int(binary, 2)
    # Convert integer to binary
    binary = bin(binary)[2:]
    return binary


if