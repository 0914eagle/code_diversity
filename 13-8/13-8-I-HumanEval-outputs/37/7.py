
def starts_one_ends(n: int) -> int:
    
    count = 0
    for i in range(1, 10):
        count += (i * 9 ** (n - 1)) + (9 * 9 ** (n - 2))
    return count

