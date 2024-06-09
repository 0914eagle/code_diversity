
def fruit_distribution(s: str, n: int) -> int:
    
    # your code here
    apple_count = int(s.split('apples and')[0])
    orange_count = int(s.split('oranges')[0].split('and ')[1])
    mango_count = n - apple_count - orange_count
    return mango_count

