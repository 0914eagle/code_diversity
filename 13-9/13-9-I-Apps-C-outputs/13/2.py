
def solve(n, k):
    count = 0
    for i in range(1, n+1):
        binary = bin(i)[2:]
        set_bits = binary.count('1')
        if set_bits == k:
            count += 1
    return count % 1000000007

