
def fruit_distribution(s: str, n: int) -> int:
    
    # your code here
    apples = s.split('apples and')[0]
    oranges = s.split('apples and')[1].split('oranges')[0]
    mangoes = n - (int(apples) + int(oranges))
    return mangoes

