
def fruit_distribution(s: str, n: int) -> int:
    
    # your code goes here
    apples, oranges = s.split(' and ')
    apples = apples.split(' ')[0]
    oranges = oranges.split(' ')[0]
    return n - (int(apples) + int(oranges))

