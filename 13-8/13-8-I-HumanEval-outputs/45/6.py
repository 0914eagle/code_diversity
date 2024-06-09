
def fruit_distribution(s: str, n: int) -> int:
    
    apples, oranges = map(int, s.split()[0].split(' and '))
    return n - apples - oranges

