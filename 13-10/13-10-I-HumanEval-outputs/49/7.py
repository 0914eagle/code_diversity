
def fruit_distribution(s: str, n: int) -> int:
    
    apples, oranges = map(int, s.split()[0:2])
    return n - apples - oranges

