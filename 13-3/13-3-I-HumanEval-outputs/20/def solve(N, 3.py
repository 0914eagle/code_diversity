
def solve(N: int) -> str:
    
    return bin(sum(int(digit) for digit in str(N)))[2:]

