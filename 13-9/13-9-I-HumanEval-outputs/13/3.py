
def fruit_distribution(s: str, n: int) -> int:
    
    apples, oranges = map(int, s.split()[:2])
    return n - apples - oranges

