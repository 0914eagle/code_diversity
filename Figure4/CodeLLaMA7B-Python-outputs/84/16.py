def solve(N):
    
    # convert N to binary
    binary = bin(N)[2:]
    # sum the digits
    sum_of_digits = sum(int(digit) for digit in binary)
    # convert the sum to binary
    return bin(sum_of_digits)[2:]


if __name__ == '__main__':
    print(solve(int(input())))
