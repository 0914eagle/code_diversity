def solve(N):
    
    # Convert the number to binary
    binary = bin(N)[2:]
    # Sum the binary digits
    total = sum([int(x) for x in binary])
    # Convert the sum to binary
    return bin(total)[2:]


if