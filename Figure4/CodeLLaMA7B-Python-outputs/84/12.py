def solve(N):
    
    # 1. check if N is a valid input
    if N < 0 or N > 10000:
        raise ValueError('N must be between 0 and 10000')
    # 2. convert N to binary
    bin_N = bin(N)[2:]
    # 3. convert binary to decimal
    dec_N = int(bin_N, 2)
    # 4. convert decimal to binary
    bin_dec_N = bin(dec_N)[2:]
    # 5. return binary
    return bin_dec_N


# test
assert solve(100