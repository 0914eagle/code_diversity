
def sum_digits_binary(N: int) -> str:
    total_sum = 0
    while N > 0:
        total_sum += N & 1
        N >>= 1
    return bin(total_sum)[2:]

if __name__ == "__main__":
    N = int(input())
    print(sum_digits_binary(N))
