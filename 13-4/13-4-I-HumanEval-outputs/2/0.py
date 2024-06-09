
def fruit_distribution(s: str, n: int) -> int:
    
    # your code here
    apples, oranges = map(int, s.split()[0].split(' '))
    return n - apples - oranges

