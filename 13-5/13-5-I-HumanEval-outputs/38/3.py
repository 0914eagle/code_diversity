
def fruit_distribution(s: str, n: int) -> int:
    
    apples, oranges = s.split(' and ')
    apples = int(apples)
    oranges = int(oranges)
    return n - apples - oranges

