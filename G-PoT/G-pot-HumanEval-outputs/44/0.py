
def solve(N: int) -> str:
    
    total_sum = sum(int(digit) for digit in bin(N)[2:])
    return bin(total_sum)[2:]
