
def sum_binary_digits(N: int) -> str:
    binary = bin(N)[2:]
    total_sum = 0
    for digit in binary:
        total_sum += int(digit)
    return bin(total_sum)[2:]

if __name__ == "__main__":
    N = int(input())
    print(sum_binary_digits(N))
