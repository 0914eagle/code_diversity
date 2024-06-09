
def f1(C, K):
    # Convert C to a string
    C_str = str(C)
    
    # Find the index of the first non-zero digit in C_str
    first_non_zero_idx = 0
    for i in range(len(C_str)):
        if C_str[i] != '0':
            first_non_zero_idx = i
            break
    
    # Find the number of digits after the first non-zero digit
    num_digits = len(C_str) - first_non_zero_idx
    
    # Round C to the nearest number that can be paid
    if num_digits > K:
        # If C has more digits than the smallest bill, round it down to the nearest multiple of 10^K
        C = int(C_str[:first_non_zero_idx] + '0' * K)
    else:
        # If C has the same number of digits as the smallest bill, round it up to the next multiple of 10^K
        C = int(C_str[:first_non_zero_idx] + '0' * K) + 10**K
    
    return C

def f2(C, K):
    # Convert C to a string
    C_str = str(C)
    
    # Find the index of the first non-zero digit in C_str
    first_non_zero_idx = 0
    for i in range(len(C_str)):
        if C_str[i] != '0':
            first_non_zero_idx = i
            break
    
    # Find the number of digits after the first non-zero digit
    num_digits = len(C_str) - first_non_zero_idx
    
    # Round C to the nearest number that can be paid
    if num_digits > K:
        # If C has more digits than the smallest bill, round it down to the nearest multiple of 10^K
        C = int(C_str[:first_non_zero_idx] + '0' * K)
    else:
        # If C has the same number of digits as the smallest bill, round it up to the next multiple of 10^K
        C = int(C_str[:first_non_zero_idx] + '0' * K) + 10**K
    
    return C

if __name__ == '__main__':
    C, K = map(int, input().split())
    print(f1(C, K))

