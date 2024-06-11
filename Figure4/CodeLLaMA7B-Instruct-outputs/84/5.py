

def solve(N):
    
    # convert N to binary
    binary = bin(N)[2:]
    # sum the digits
    sum = 0
    for digit in binary:
        sum += int(digit)
    # return the sum in binary
    return bin(sum)[2:]


