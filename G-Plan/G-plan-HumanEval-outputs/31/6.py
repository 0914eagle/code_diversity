
def sum_binary_digits(N: int) -> str:
    total_sum = 0
    while N:
        total_sum += N & 1
        N >>= 1
    return bin(total_sum)[2:]

if __name__ == "__main__":
    N = int(input())
    print(sum_binary_digits(N))
