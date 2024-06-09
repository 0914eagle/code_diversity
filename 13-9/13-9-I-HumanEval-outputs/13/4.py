
def fruit_distribution(s: str, n: int) -> int:
    
    apples, oranges = s.split()[0], s.split()[4]
    return n - int(apples) - int(oranges)

