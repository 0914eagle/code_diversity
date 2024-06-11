def solve(N):
    
    # 1. check the input
    if N < 0 or N > 10000:
        raise ValueError('N should be between 0 and 10000')
    # 2. solve the problem
    # 2.1. convert the number to binary
    binary_number = bin(N)[2:]
    # 2.2. sum the digits
    total_sum = 0
    for digit in binary_number:
        total_sum += int(digit)
    # 3. return the result
    return bin(total_sum)[2:]


# test
# print