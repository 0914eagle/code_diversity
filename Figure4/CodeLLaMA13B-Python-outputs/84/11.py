def solve(N):
    
    # Convert to binary
    binary = bin(N)[2:]
    # Sum the digits
    total = sum([int(x) for x in binary])
    # Convert to binary again
    return bin(total)[2:]

if