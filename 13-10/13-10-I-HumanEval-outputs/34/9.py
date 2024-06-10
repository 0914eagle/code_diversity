
def modp(n: int, p: int) -> int:
    
    result = 1
    for i in range(n):
        result = (result * 2) % p
    return result

