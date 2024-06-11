

def solve(N):
    
    # convert N to binary
    binary = bin(N)[2:]
    # sum the digits
    sum_of_digits = sum([int(digit) for digit in binary])
    # return the sum as a binary number
    return bin(sum_of_digits)[2:]


