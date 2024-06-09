
def starts_one_ends(n: int) -> int:
    
    count = 0
    for i in range(1, 10):
        count += (10**(n-1)) * i
        count += i * (10**(n-1))
    return count

