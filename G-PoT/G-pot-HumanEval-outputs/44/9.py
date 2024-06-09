
def solve(N: int) -> str:
    binary_sum = sum(int(digit) for digit in bin(N)[2:])
    return bin(binary_sum)[2:]
