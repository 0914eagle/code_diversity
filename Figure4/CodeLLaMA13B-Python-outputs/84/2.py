def solve(N):
    
    # Convert the integer to binary
    binary = bin(N)[2:]
    # Sum the binary digits
    total = sum([int(i) for i in binary])
    # Convert the sum to binary
    return bin(total)[2:]

if