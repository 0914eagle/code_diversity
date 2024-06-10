
def solve(N: int) -> str:
    total_sum = 0
    while N > 0:
        total_sum += N & 1
        N >>= 1
    return bin(total_sum)[2:]
