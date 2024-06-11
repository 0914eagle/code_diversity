

def solve(N):
    
    # convert N to binary
    binary = bin(N)[2:]
    # sum the digits
    total = sum([int(digit) for digit in binary])
    # return the total as a binary string
    return bin(total)[2:]


