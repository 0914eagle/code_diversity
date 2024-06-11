def solve(N):
    
    # 1. check if N is a positive integer
    if N < 0:
        return "ERROR"
    # 2. convert N to binary
    binary_N = bin(N)[2:]
    # 3. sum the digits of binary_N
    sum_of_digits = sum([int(digit) for digit in binary_N])
    # 4. convert sum_of_digits to binary
    binary_sum_of_digits = bin(sum_of_digits)[2:]
    # 5. return binary_sum_of_digits
    return binary_sum_of_digits


#