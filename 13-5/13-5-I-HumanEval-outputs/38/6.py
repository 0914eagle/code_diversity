
def fruit_distribution(s: str, n: int) -> int:
    
    # your code here
    apples, oranges = map(int, s.split()[:2])
    return n - apples - oranges

